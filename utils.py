import sqlite3
from datetime import *
from PIL import Image, ImageDraw, ImageFont
import random
import string
import os
from flask import render_template
import logging

def getban():
    f = open("./data/banlist.txt", 'r', encoding = 'utf-8')
    r = f.readlines()
    f.close()
    return r

def b_render(content):
    bs = getban()
    for b in bs:
        content = content.replace(b.replace('\n', ''), '***')
    
    content = content.replace("\n", "   ")
    content = content.replace(r"\\", '\\')

    content = content.replace("\\==", "[高亮]")
    content = content.replace("\\=?", "")
    content = content.replace("\\>", "[引用]")
    content = content.replace("\\>>", "")
    content = content.replace(r"\##", "[标题]")
    content = content.replace(r"\@@", "")
    content = content.replace(r"\#", "[小标题]")
    content = content.replace(r"\@", "")
    content = content.replace(r"\*\*", "[粗体]")
    content = content.replace(r"\*", "")
    content = content.replace(r"\?\?", "[斜体]")
    content = content.replace(r"\?", "")
    content = content.replace(r"\_\_", "[下划线]")
    content = content.replace(r"\_", "")
    content = content.replace(r"\+", "[链接]")
    content = content.replace(r"\-", "")
    content = content.replace(r"\=", "")

    content = content.replace("\\![", "[图片]")
    content = content.replace("\\]", "")

    content = content.replace("\\/", "[文件]")
    content = content.replace("\\~", "")

    # content = content.replace("\\+", "<a href = \"")
    # content = content.replace("\\-", "\">")

    return content


def render(content: str, tmp=False, learn=False):
    bs = getban()
    for b in bs:
        content = content.replace(b, '***')
    
    '''
    # 避免嵌入式script攻击
    content = content.replace("<script", "这是script的开头")
    content = content.replace("</script>", "这是script的末尾")
    content = content.replace("\n", "<br />")
    content = content.replace("\\\\", "\\")
    content = content.replace("\\<script", "<script")
    content = content.replace("\\</script>", "</script>")
    '''
    
    content = content.replace("\\<script>", "<script>")
    content = content.replace("\\</script>", "</script>")
    
    
    content = content.replace("\n", "<br />")
    content = content.replace("\\\\", "\\")
    
    content = content.replace("\\==", "<mark>")
    content = content.replace("\\=?", "</mark>")
    content = content.replace("\\>>", "</blockquote>")
    content = content.replace("\\>", "<blockquote>")
    content = content.replace("\\##", "<h2>")
    content = content.replace("\\@@", "</h2>")
    content = content.replace("\\#", "<h3>")
    content = content.replace("\\@", "</h3>")
    content = content.replace("\\*\\*", "<strong>")
    content = content.replace("\\*", "</strong>")
    content = content.replace("\\?\\?", "<i>")
    content = content.replace("\\?", "</i>")
    content = content.replace("\\_\\_", "<u>")
    content = content.replace("\\_", "</u>")
    content = content.replace("\\+", "<a href = \"")
    content = content.replace("\\-", "\">")
    content = content.replace("\\/", "<a href = \"path")
    content = content.replace("\\~", '\" download>')
    content = content.replace("\\=", "</a>")

    if tmp or learn:
        content = content.replace("\\![", "<img src = \"../../../static/discuss_img/")
        content = content.replace("path", "../../../static/discuss_file/")
    else:
        content = content.replace("\\![", "<img src = \"../../static/discuss_img/")
        content = content.replace("path", "../../static/discuss_file/")
    content = content.replace("\\]", "\" />")
    # content = content.

    # content = content.replace("\\+", "<a href = \"")
    # content = content.replace("\\-", "\">")

    return content


def get_cursor():
    if not os.path.exists('./database_name.txt'):
        name = 'database'
    else:
        f = open("./database_name.txt", "r", encoding='utf-8')
        name = f.read()
        f.close()
    conn = sqlite3.connect(f"./{name}.db")
    cursor = conn.cursor()
    return conn, cursor


def all_users():
    c = get_cursor()
    c[1].execute("SELECT * FROM users")
    aus = c[1].fetchall()
    kd = []
    for au in aus:
        kd.append(str(au[0]))
    c[0].commit()
    c[0].close()
    return ','.join(kd)


def get_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_temp_list():
    tmp_lst = open("./templist.txt", "r", encoding="utf-8")
    temp_list = tmp_lst.read().split(',')
    tmp_lst.close()
    return temp_list

def generate_captcha_image():
    # 定义图片大小及背景颜色
    image = Image.new('RGB', (100, 30), color=(200, 180, 210))

    # 使用系统自带字体，或指定字体文件路径
    font_path = "./static/css/HW_NEW.TTF"
    fnt = ImageFont.truetype(font_path, 16)
    d = ImageDraw.Draw(image)

    # 生成5位数的验证码文本
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    d.text((15, 10), captcha_text, font=fnt, fill=(255, 20, 155))

    # 添加干扰线条和噪点
    for _ in range(random.randint(4, 6)):
        start = (random.randint(0, image.width), random.randint(0, image.height))
        end = (random.randint(0, image.width), random.randint(0, image.height))
        d.line([start, end], fill=(random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)))

    for _ in range(100):
        xy = (random.randrange(0, image.width), random.randrange(0, image.height))
        d.point(xy, fill=(random.randint(50, 200), random.randint(50, 200), random.randint(50, 200)))

    return image, captcha_text
