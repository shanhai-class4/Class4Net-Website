# -*- coding: UTF-8 -*-
import sqlite3
from database import *
from utils import *
from flask import *
import flask
from database import *
import string
import random
from datetime import *
import os
import os.path
import shutil
import random
import cv2
import numpy
from utils import *
import shelve
import io
from wsgiref.simple_server import make_server
from dsearch import *
import logging
import glob

# from database import *
# c = get_cursor()
# # 初始化
# cursor = c[1]
# cursor.execute("DROP TABLE IF EXISTS users;")
# cursor.execute("""CREATE TABLE users (
# id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
# username TEXT NOT NULL,
# password TEXT NOT NULL,
# name TEXT NOT NULL,
# level INT NOT NULL,
# score INT NOT NULL,
# active INT NOT NULL,
# admin INT NOT NULL,
# picpath TEXT NOT NULL,
# desc TEXT
# );""")
#
# cursor.execute("DROP TABLE IF EXISTS discuss;")
# cursor.execute("""CREATE TABLE discuss (
# id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
# father INT,
# title TEXT,
# subject TEXT,
# date TEXT NOT NULL,
# pub INT NOT NULL,
# csee TEXT NOT NULL,
# top INT NOT NULL,
# temp INT NOT NULL,
# fname TEXT,
# desc TEXT
# );""")
#
# cursor.execute("DROP TABLE IF EXISTS resource;")
# cursor.execute("""CREATE TABLE resource (
# id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
# father INT,
# title TEXT,
# subject TEXT,
# date TEXT NOT NULL,
# pub INT NOT NULL,
# csee TEXT NOT NULL,
# top INT NOT NULL,
# temp INT NOT NULL,
# fname TEXT,
# desc TEXT
# );""")
#
# f = open('templist.txt', 'w', encoding='utf-8', newline = '\n')
# f.write('')
# f.close()

# cursor.execute(
#     "INSERT INTO discuss (id, title, subject, date, pub, csee, top, temp) VALUES (1, '班级圈网站规定', '公告,班级圈,官方,帮助文档', '2024-7-12 17:00:00', 49, 'all', 1, 0)")
# cursor.execute(
#     "INSERT INTO discuss (id, title, subject, date, pub, csee, top, temp) VALUES (2, '2024，属于你的暑假生活', '公告,征集', '2024-7-12 17:00:00', 49, 'all', 1, 0)")
# cursor.execute(
#     "INSERT INTO discuss (id, title, subject, date, pub, csee, top, temp) VALUES (3, '班级圈发布会', '公告,班级圈,官方', '2024-7-12 17:00:00', 49, 'all', 1, 0)")
# cursor.execute(
#      "INSERT INTO discuss (id, title, subject, date, pub, csee, top, temp) VALUES (4, '今日作业', '公告,作业', '2024-7-12 17:00:00', 49, 'all', 1, 0)")
# cursor.execute("INSERT INTO discuss (id, father, title, subject, date, pub, csee, top, temp) VALUES (5, 3, '期待班级圈发布会精彩表现', '班级圈,测试', '2024-7-12 18:00:00', 49, 'all', 1, 0)")

# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('张博充', '201010280016', '曹博充', 0, 0, 0, 0, '1.png', '四时之景不同，<br>而乐亦无穷也。')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('陈思羽Gina', 'Gina0727', '陈思羽', 0, 0, 0, 0, '2.png', '斯人若彩虹，遇上方知有。')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('0V0', '20101012hjh', '程钟灵', 0, 0, 0, 1, '3.png', 'IIIIIIIIIIlllllllllIIIIIIIIIlllllll！！！！！！！！')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('Darin', '100929', '达宸滋', 0, 0, 0, 1, '4.png', 'I love orange！')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('青山不老', '123456', '翟培龙', 0, 0, 0, 1, '5.png', '这里的云等风，我却在等你')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('Aurora', 'Founder0415', '丁一宁', 0, 0, 0, 0, '6.png', '身在井隅  心向璀璨')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('想飞的蓝猫子', 'dyc20110529', '董雨宸', 0, 0, 0, 1, '7.png', '三天打鱼，两天晒网')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('付敬卯', 'marvin0301', '付敬卯', 0, 0, 0, 0, '8.png', '有志者，事竟成')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('萨卡班甲鱼', '114514', '甘宇轩', 0, 0, 0, 1, '9.png', '喵喵喵？')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('高一凡', 'gyf780725', '高一凡', 0, 0, 0, 0, '10.png', '一球入魂')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('郭益昕', 'gyx20110304', '郭益昕', 0, 0, 0, 0, '11.png', '无')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('Samuel墨', '232323', '郝翌墨', 0, 0, 0, 0, '12.png', '既然目标是地平线，留给世界的只能是背影')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('胡堇暄', '110112201102096426a', '胡堇暄', 0, 0, 0, 0, '13.png', '无')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('江篱辟芷', '20110614hjy', '胡峻瑛', 0, 0, 0, 1, '14.png', '我似浮云滞吴越，君逢圣主游丹阙。<br><br>欲填沟壑唯疏放，自笑狂夫老更狂。')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('HYH', '201119', '华毅弘', 0, 0, 0, 0, '15.png', '没有个性')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('1234567', '1234567', '黄一寻', 0, 0, 0, 1, '16.png', '不被踩在脚下')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('姜皓程', '20110131', '姜皓程', 0, 0, 0, 0, '17.png', '我是姜皓程')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('卡乐星', 'tt110316', '孔令煊', 0, 0, 0, 0, '18.png', '再渺小的同频<br>都是最感动的爱<br>以爱之名<br>你还愿意吗')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('lccccc.', '951218', '李畅', 0, 0, 0, 0, '19.png', '️️')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('XiaoLi', 'XieLi&1104@BJQ#666', '李东泽', 0, 0, 0, 1, '20.png', '666这个入开桂了')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('李亦凡', 'liyifan0421', '李亦凡', 0, 0, 0, 0, '21.png', '我叫李亦凡 我热爱乒乓球 竹笛')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('雒贝西', '813924', '雒贝西', 0, 0, 0, 0, '22.png', '生命不息，奋斗不止。')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('钱薇涵', 'qwh517621815', '钱薇涵', 0, 0, 0, 0, '23.png', '钱薇涵<br>上帝一声不响，一切皆有我定.&Heliotrope.')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('小迪', 'Cindy1109', '曲昕迪', 0, 0, 0, 0, '24.png', '喵。为什么不可以修改个性签名哇啊啊啊啊啊')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('戎佳佳', '我是老六！！！', '戎佳怡', 0, 0, 0, 0, '25.png', '༼·⍨༽༼·∵༽༼· ͒ ͓ ͒༽༼· ͒ ̶ ͒༽༼·⍢༽༼·⍤༽')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('沈树阳', '201181', '沈树阳', 0, 0, 0, 0, '26.png', '厚积薄发，茁壮成长')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('孙毓彤', '0208', '孙毓彤', 0, 0, 0, 0, '27.png', '你要做站在云上的那个人<br>站在太阳和月亮之间<br>做最明亮的那一个人')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('王岩杉', 'Wys201010276367.', '王岩杉', 0, 0, 0, 1, '28.png', '和光同尘<br>光而不耀')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('王予清', '201012', '王予清', 0, 0, 0, 0, '29.png', 'What can I say')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('我是王元基', '123456', '王元基', 0, 0, 0, 0, '30.png', '我应该是王元基吧')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('许可', 'x11320', '许可', 0, 0, 0, 1, '31.png', \"What doesn't kill me makes me want more.\")")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('闫嘉桐', 'Yan.J.T.110101', '闫嘉桐', 0, 0, 0, 1, '32.png', '太阳照常升起，一切都没有改变')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('杨晨曦', '0114', '杨晨曦', 0, 0, 0, 0, '33.png', '我是杨晨曦，性格活泼开朗，有许多爱好，如：美术、书法、吉他等。')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('kyd_逃跑程序员', 'yhj20110320', '尹怀杰', 0, 0, 0, 1, '34.png', '不把个性签名不能修改的bug修复了不改签名！')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('贠涵', 'Yh20110217', '贠涵', 0, 0, 0, 1, '35.png', '。')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('烟雨一蓑', '20110202', '袁立之', 0, 0, 0, 1, '36.png', '我喜欢chatGPT<br>chatGPT yyds')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('B612', '20101025B612', '张飞扬', 0, 0, 0, 0, '37.png', 'TuT。')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('你的东西在哪里？', 'zmy20101226', '张茂原', 0, 0, 0, 0, '38.png', '你的就是我的，我的还是我的')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('ztz.', '412313', '张天字', 0, 0, 0, 0, '39.png', '如果你追不着光，就自己努力成为自己的光')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('张惜媛', 'zxy101018', '张惜媛', 0, 0, 0, 0, '40.png', '我叫张惜媛。日常生活中，我爱好广泛，喜欢弹琴、打羽毛球。')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('天戾V', '110708', '张益弘', 0, 0, 0, 0, '41.png', '我叫张益弘，生于2011，')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('十三月', 'bjj+141592', '张竹青', 0, 0, 0, 0, '42.png', '至我们鱼死网破的胜利┐(T.T ) ( T.T) ノ')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('Z.', '0221', '张茁原', 0, 0, 0, 1, '43.png', 'To reach the unreachable star By一个笑点极低，笑声魔性的中学生')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('一颗樟脑丸', 'tangxr_0227', '赵泽晓', 0, 0, 0, 0, '44.png', '生命的跋涉不能回头，哪怕畏途巉岩不可攀，也要会当凌绝顶。')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('听凭风引', '0417zhouyushu', '周玉姝', 0, 0, 0, 0, '45.png', '愿风神忽悠你～')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('最高级管理员', 'admin', '管理员', 0, 0, 0, 1, '46.png', '我是最高级管理员')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('班主任谢老师', '123456', '谢宝琴', 0, 0, 0, 1, '47.png', '谢老师的官方账号')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('游客', '123456', '来自别的班的游客', 0, 0, 0, 0, '48.png', '如果有别的班游客想游览班级圈，请登录本账号')")
# cursor.execute("INSERT INTO users (username, password, name, level, score, active, admin, picpath, desc) VALUES ('班级圈官方', 'bjq_project', '班级圈', 0, 0, 0, 1, '49.png', '大家好，我是班级圈计划的官方账号，会发布精彩的文章、资源和开发进度！')")
# c[0].commit()
# c[0].close()

def deldir(path):
    shutil.rmtree(path)
    os.mkdir(path)

def refill(path, con = ''):
    f = open(path, 'w', encoding='utf-8', newline = '\n')
    f.write(con)
    f.close()

# deldir('./data/activity')
# refill('./data/activity.txt')
# refill('./data/album.txt')
# refill('./data/banlist.txt')
refill('./data/code.txt')
# refill('./data/edit_hold_publisher.txt', 'F')
# refill('./data/homework.txt', '1\n1')
# refill('./data/index.txt')
# refill('./data/learn.txt')
# refill('./data/news_id.txt')
# refill('./data/redt.txt')
# refill('./data/tops_info.txt', """1.png
# A
# B
# /discuss/1/
# 1.png
# C
# D
# /discuss/1/
# 1.png
# E
# F
# /discuss/1/""")
deldir('./discuss')
deldir('./discussform')
# deldir('./group')
# refill('./group_cnt.txt', '0')
deldir('./resource')
deldir('./static/discuss_img')
deldir('./static/discuss_file')
for item in os.listdir('./static/album/'):
    item_path = os.path.join('./static/album/', item)
    if os.path.isdir(item_path):
        deldir(item_path)

os.remove('./0.db')