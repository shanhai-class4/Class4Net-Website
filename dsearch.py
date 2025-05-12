import jieba
import re
from collections import defaultdict
from database import *
import shelve
import os
import logging


class TrieNode:
    def __init__(self):
        self.children = {}
        self.post_ids = set()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, post_id):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.post_ids.add(post_id)

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return set()  # 没有找到前缀
        return self._collect_post_ids(node)

    def _collect_post_ids(self, node):
        result_set = set(node.post_ids)
        for child_node in node.children.values():
            result_set.update(self._collect_post_ids(child_node))
        return result_set


def is_chinese(word):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    return bool(pattern.search(word))


def tokenize(text):
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower().split()


def split_content(content):
    # 去除HTML标签
    content = re.sub(r'<[^>]+>', '', content)

    # 去除标点符号
    content = re.sub(r'[，。！？、（）《》【】<>“”‘’：…；~～\-*#@.,!?()"\'\[\]{}\\]—_', '', content)
    content = content.replace("\n", "")
    chinese_words = []
    english_words = []
    words = jieba.lcut(content)
    for word in words:
        if all(is_chinese(char) for char in word):
            chinese_words.append(word)
        elif word.strip():  # 确保不添加空白字符
            english_words.append(word.lower())
    return chinese_words, english_words


def calculate_tf(posts):
    """
    计算每篇文档的词频向量
    """
    tf_vectors = {}
    for post in posts:
        post_id = post['id']
        content = [i for i in jieba.lcut(post['content']) if i != ' ']
        print("Split Content:", content)
        tf = defaultdict(int)
        for word in content:
            tf[word] += 1
        tf_vectors[post_id] = tf
    return tf_vectors


def build_tries(posts):
    chinese_trie = Trie()
    english_trie = Trie()

    for post in posts:
        post_id = post['id']
        content = post['content']
        chinese_words, english_words = split_content(content)

        # 插入中文和英文单词
        unique_chinese_words = set(chinese_words)
        unique_english_words = set(english_words)

        for word in unique_chinese_words:
            chinese_trie.insert(word, post_id)

        for word in unique_english_words:
            english_trie.insert(word, post_id)

        # 仅对有实际意义的短语进行部分匹配处理，避免插入所有短语组合
        # 例如，只插入固定长度的短语，或基于一些规则选择插入的短语
        for i in range(len(chinese_words)):
            if i + 2 <= len(chinese_words):  # 仅插入2词短语（可以根据需求调整）
                phrase = ''.join(chinese_words[i:i + 2])
                chinese_trie.insert(phrase, post_id)
        print(f"Inserting word '{word}' into Trie")

        for i in range(len(english_words)):
            if i + 2 <= len(english_words):  # 仅插入2词短语（可以根据需求调整）
                phrase = ''.join(english_words[i:i + 2])
                english_trie.insert(phrase, post_id)

    return {'chinese': chinese_trie, 'english': english_trie}


def add_document_to_search_tree(new_post, tries, tf_vectors):
    # 获取新帖子内容
    post_id = new_post['id']
    content = new_post['content']

    # 更新词频向量
    new_tf = defaultdict(int)
    words = jieba.lcut(content)  # 使用分词工具
    for word in words:
        if word.strip():  # 确保不添加空白字符
            new_tf[word] += 1
    tf_vectors[post_id] = new_tf

    # 更新搜索树
    chinese_words, english_words = split_content(content)

    # 插入中文和英文单词到现有树中
    for word in set(chinese_words):
        tries['chinese'].insert(word, post_id)

    for word in set(english_words):
        tries['english'].insert(word, post_id)

    # 插入短语
    for i in range(len(chinese_words)):
        if i + 2 <= len(chinese_words):
            phrase = ''.join(chinese_words[i:i + 2])
            tries['chinese'].insert(phrase, post_id)

    for i in range(len(english_words)):
        if i + 2 <= len(english_words):
            phrase = ''.join(english_words[i:i + 2])
            tries['english'].insert(phrase, post_id)

    # 将更新后的搜索树和词频向量写回数据库
    return tries, tf_vectors


def tree_search(query, tries, tf_vectors, scale_factor=100):
    words = jieba.lcut(query.lower())
    search_results = defaultdict(float)

    # 进行单个词汇匹配
    query_vector = defaultdict(int)
    for word in words:
        if all(is_chinese(char) for char in word):  # 中文查询
            post_ids = tries['chinese'].search(word)
            for post_id in post_ids:
                query_vector[word] += 1
        else:  # 英文查询
            post_ids = tries['english'].search(word)
            for post_id in post_ids:
                query_vector[word] += 1

    for post_id, doc_vector in tf_vectors.items():
        # 计算词汇匹配度
        tf_score = sum(query_vector[word] * doc_vector.get(word, 0) for word in query_vector if word in doc_vector)
        if tf_score == 0:
            continue

        query_norm = sum(value ** 2 for value in query_vector.values()) ** 0.5
        doc_norm = sum(value ** 2 for value in doc_vector.values()) ** 0.5

        if query_norm == 0 or doc_norm == 0:
            continue

        tf_score /= (query_norm * doc_norm)

        # 将匹配度加入结果
        search_results[post_id] += tf_score

    # 过滤掉匹配度为 0 的结果
    search_results = {post_id: score for post_id, score in search_results.items() if score > 0}

    # 乘以常数因子，使得所有结果大于1
    for post_id in search_results:
        search_results[post_id] *= scale_factor

    sorted_results = sorted(search_results.items(), key=lambda x: x[1], reverse=True)
    return sorted_results


# 这个函数是用来把数据写入数据库的
def data_write(tries, tf_vectors):
    with shelve.open('./dsearch/dsearch') as db:
        db['chinese_trie'] = tries['chinese']
        db['english_trie'] = tries['english']
        db['tf_vectors'] = {'t': tf_vectors}


# 这个函数是用来读取数据库的
def data_read():
    with shelve.open('./dsearch/dsearch') as db:
        chinese_trie = db['chinese_trie']
        english_trie = db['english_trie']
        tf_vectors = db['tf_vectors']['t']
    return {'chinese': chinese_trie, 'english': english_trie}, tf_vectors


# 这个函数是用来创建搜索树的，可以在新增帖子时运行
def set_search_tree():
    posts = []
    discuss_file_list = os.listdir('./discuss/')
    for i in discuss_file_list:
        discuss_id = int(i.split('.txt')[0])
        posts.append({'id': discuss_id, 'content': get_discuss(discuss_id)})
        print(f"Pending - discuss {discuss_id}.txt Loading...")
    tries = build_tries(posts)
    tf_vectors = calculate_tf(posts)
    data_write(tries, tf_vectors)


# 增量更新搜索树的函数
def add_new_post(new_post):
    # 从数据库中读取现有的搜索树和词频向量
    tries, tf_vectors = data_read()
    tree = add_document_to_search_tree(new_post, tries, tf_vectors)
    data_write(tree[0], tree[1])


# 这个函数是用来通过搜索返回论坛列表的
def content_search(query, tries, tf_vectors, scale_factor):
    c = get_cursor()
    results = tree_search(query, tries, tf_vectors, scale_factor)
    print("Search results for '{}':".format(query))
    for result in results:
        print("Post ID:", result[0], "Score:", result[1])
    dis_ls = []
    for i in results:
        c[1].execute(f"SELECT * FROM discuss WHERE id = {i[0]}")
        # print(c[1].fetchall())
        try:
            dis_ls.append([c[1].fetchall()[0], i[1]])
        except IndexError:
            pass
    # return [for i in dis_ls if i[7]]
    for i in range(len(dis_ls)):
        if dis_ls[i][0][7]:
            dis_ls[i][1] *= 2
    dis_ls = sorted(dis_ls, key=lambda x: x[1], reverse=True)
    dis_ls = [Discuss(i[0][0]) for i in dis_ls]
    print(dis_ls)
    c[0].commit()
    c[0].close()
    return dis_ls


# 这个函数是用来整合搜索的
def complex_search(query):
    tries, tf_vectors = data_read()
    return content_search(query, tries, tf_vectors, 100)


# 这个函数是用来添加搜索树的
def add_search_tree(new_discuss: Discuss):
    add_new_post({'id': new_discuss.id, 'content': new_discuss.all_data})


if __name__ == '__main__':
    set_search_tree()
#     posts = [
#         {'id': 1, 'content': '''亲爱的同学们：
# 大家好！
# 欢迎访问2023级四班班级圈网站！为了营造一个安全、友好和积极的线上交流环境，请大家fo'''},
#         {'id': 2,
#          'content': '''Hello everyone! Welcome to our class website for the 2023 school year. We hope to create a
#          safe, friendly, and positive online community for all students. follow me! fo fo'''},
#         {'id': 3, 'content': '''全座椅班级'''}
#     ]
#
#     tf_vectors = calculate_tf(posts)
#     tries = build_tries(posts)
#     query = "班级"
#     results = tree_search(query, tries, tf_vectors, scale_factor=100)
#     print("Search results for '{}':".format(query))
#     for result in results:
#         print("Post ID:", result[0], "Score:", result[1])
#
#     query = "fo"
#     results = tree_search(query, tries, tf_vectors, scale_factor=100)
#     print("Search results for '{}':".format(query))
#     for result in results:
#         print("Post ID:", result[0], "Score:", result[1])
