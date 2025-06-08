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
import random
import cv2
import numpy
from utils import *
import shelve
import io
#from flask_mail import Mail, Message
from wsgiref.simple_server import make_server
from dsearch import *
import logging

file_handler = logging.FileHandler('runtime.log')  # 写入当前文件所在目录的文件，没有自动创建
file_handler.setLevel(logging.DEBUG)
# 配置控制台输出日志处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s root [%(pathname)s line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='runtime.log',
    filemode='w')

# # 配置 Werkzeug（Flask 的底层 WSGI 工具包）的日志记录器
# werkzeug_logger = logging.getLogger('werkzeug')
# werkzeug_formatter = logging.Formatter('%(asctime)s root [%(pathname)s line:%(lineno)d] %(levelname)s %(message)s')
# werkzeug_logger.addHandler(file_handler)  # 将日志输出写入文件
# werkzeug_logger.addHandler(console_handler)  # 将请求接口的状态日志也输出到控制台



# test codes & reload codes
# '''

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
#
#
# cursor.execute(
#     "INSERT INTO discuss (id, title, subject, date, pub, csee, top, temp) VALUES (1, '班级圈网站规定', '公告,班级圈,官方,帮助文档', '2024-7-12 17:00:00', 49, 'all', 1, 0)")
# cursor.execute(
#     "INSERT INTO discuss (id, title, subject, date, pub, csee, top, temp) VALUES (2, '2024，属于你的暑假生活', '公告,征集', '2024-7-12 17:00:00', 49, 'all', 1, 0)")
# cursor.execute(
#     "INSERT INTO discuss (id, title, subject, date, pub, csee, top, temp) VALUES (3, '班级圈发布会', '公告,班级圈,官方', '2024-7-12 17:00:00', 49, 'all', 1, 0)")
# cursor.execute(
#      "INSERT INTO discuss (id, title, subject, date, pub, csee, top, temp) VALUES (4, '今日作业', '公告,作业', '2024-7-12 17:00:00', 49, 'all', 1, 0)")
# cursor.execute("INSERT INTO discuss (id, father, title, subject, date, pub, csee, top, temp) VALUES (5, 3, '期待班级圈发布会精彩表现', '班级圈,测试', '2024-7-12 18:00:00', 49, 'all', 1, 0)")
# # logging.info(str(cursor.lastrowid))
#
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


def randstr(charset=list(string.ascii_lowercase + string.ascii_uppercase + string.digits), k=24):
    return ''.join(random.choices(charset, k=24))


app = Flask(__name__)
app.config['SECRET_KEY'] = "74CNYMBDSLP-20240712"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "dyc05291025@163.com"
app.config['MAIL_PASSWORD'] = "VSJIZBROIPGRDGRH"
app.config['MAIL_DEFAULT_SENDER'] = "dyc05291025@163.com"


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('.//', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

debugrun = False
if os.path.exists('./__debug.txt'):
    f = open("./__debug.txt", 'r', encoding='utf-8')
    a = f.read()
    f.close()
    if a == 'T':
        debugrun = True
    else:
        debugrun = False
else:
    debugrun = False

# mail = Mail()
# mail.init_app(app)
# session.permanent = True

id = 1
forget_password_list = []
'''
session = {}
id : int
login : True / False
admin : True / False
username : 'admin114514'
'''


@app.before_request
def default_session():
    if 'id' not in session:
        session['id'] = -1
    if 'login' not in session:
        session['login'] = False
    if 'admin' not in session:
        session['admin'] = False
    if 'capt_code' not in session:
        session['capt_code'] = None
    if 'login_times' not in session:
        session['login_times'] = 0


@app.route('/')
def index():
    file = open("./data/tops_info.txt", 'r', encoding="utf-8")
    #print(file.readlines())
    cpi1, word1, swd1, link1, cpi2, word2, swd2, link2, cpi3, word3, swd3, link3 = file.readlines()
    file.close()
    file = open("./data/homework.txt", 'r', encoding="utf-8")
    hwid, hwpid = file.readlines()
    file.close()
    file = open("./data/redt.txt", 'r', encoding="utf-8")
    raw_grs = file.readlines()
    file.close()
    cooked_grs = []
    for rg in raw_grs:
        cooked_grs.append(rg.split(' '))
    d, d2 = all_discuss(0, None, session['id'], True)
    d.extend(d2)
    d = sorted(d, key=lambda s: s[4])
    showd = []
    for i in range(min(len(d), 5)):
        showd.append(Discuss(d[i][0]))
    with open('./data/activity.txt', 'r', encoding="utf-8") as file:
        new_act = file.read().split('\n')
        new_act = [i.split(':') for i in new_act]
    res = all_resource()[1]
    res_list = []
    logging.info(str(res))
    for i in range(min(len(res), 5)):
        res_list.append(Resource(res[i][0]))
    showd = [i for i in showd if '评论回复' not in i.subject]
    
    i = 1
    nimg_src = ""
    nimg_date = ""
    nidt = 0
    while True:
        if not os.path.exists(f'./static/album/{i}/'):
            break
        else:
            imf = os.listdir(f"./static/album/{i}/")
            for j in imf:
                path = f'album/{i}/{j}'
                fpath = f'./static/album/{i}/{j}'
                dt = os.path.getctime(fpath)
                if dt > nidt:
                    nidt = dt
                    nimg_src = path
                    nimg_date = datetime.fromtimestamp(dt)
        i += 1
        #strftime("%Y-%m-%d %H:%M:%S")
    
    return render_template("index.html", session=session, cex_picid1 = cpi1, cex_picid2 = cpi2, cex_picid3 = cpi3, cex_words_1=word1, cex_words_2=word2, cex_words_3=word3,
                           cex_link_1=link1, cex_link_2=link2, cex_link_3=link3,cex_swd1=swd1, cex_swd2=swd2, cex_swd3=swd3, hwid=hwid, hwpid=hwpid, grs=cooked_grs,
                           dis=showd, act=new_act, res=res_list, xc = (nimg_src, nimg_date))


@app.route('/debug/')
def debug():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    return render_template("debug.html", session=session, content='You have not read any file.', d1="---", d2="---")


@app.route("/debug/handle1/", methods=['POST'])
def debug_handle1():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    name = request.form.get('docname', '')
    if name == "main.py":
        return render_template("debug.html", session=session,
                               content="Error: You cannot edit main.py, because it is the main program file in this project!",
                               d1="---", d2="---")
    try:
        with open(f"./{name}", "r", encoding='utf-8') as f:
            con = f.read()
        if 'html' not in name:
            con = con.replace('\n', '<br>')
        else:
            con += '<HTMLELE>'
    except:
        return render_template("debug.html", session=session, content=f"Error: No such file or directory : {name}",
                               d1="---", d2="---")
    return render_template("debug.html", session=session, content=con, d1="---", d2="---")


@app.route("/debug/handle2/", methods=['POST'])
def debug_handle2():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    name = request.form.get('docname', '')
    con = request.form.get('txt', '')
    if name == "main.py":
        return render_template("debug.html", session=session, content="You have not read any file.",
                               d1="[Error] You cannot edit main.py, because it is the main program file in this project!",
                               d2="---")
    if not os.path.exists(name):
        return render_template("debug.html", session=session, content="You have not read any file.",
                               d1=f"[Error] No such file or directory : {name}", d2="---")
    try:
        with open(f"./{name}", "w", encoding='utf-8', newline = '\n') as f:
            f.write(con)
    except Exception as err:
        return render_template("debug.html", session=session, content="You have not read any file.",
                               d1=f"[Error] Unknown Exception: {err}", d2="---")

    return render_template("debug.html", session=session, content='You have not read any file.', d1="[Info] edit correctly", d2="---")


@app.route('/debug/handle3/', methods=['POST'])
def debug_handle_3():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    cmd = request.form.get('SQL', '')
    c = get_cursor()
    cursor = c[1]
    d = ''
    try:
        cursor.execute(cmd)
    except sqlite3.OperationalError:
        # break
        d += f"[Error] SQL Operation Error - No such code : '{cmd}';<br>"
    except Exception as err:
        d += f"[Fatal] Unknown Error - Error data : <br> {err} <br>"
        d += f"SYS EXC_INFO DATA: {sys.exc_info()[0]} <br> -------------------<br>"
    else:
        d += "[Info] SQL Operation;<br>"
    d += f"[Info] Cursor Fetchall : '{cursor.fetchall()}';<br>"
    c[0].commit()
    c[0].close()
    return render_template("debug.html", session=session, content='You have not read any file.',
                           d1="---", d2=d)


# @app.route('/mail/test/')
# def mail_test():
#     message = Message(subject="test", recipients=['13021262946@163.com'], body="有人使用了mail_test路由；hello, world!")
#     mail.send(message)
#     message = Message(subject="test", recipients=['2247286854@qq.com'], body="有人使用了mail_test路由；hello, yhj!")
#     mail.send(message)
#     return "邮件发送成功！"

'''
@app.route('/lookforsession/')
def lsessioner():
    logging.info(str(session['login']) + str(session['id']))
    return session


@app.route('/lookforuser/')
def luser():
    u = User(session['id'])
    logging.info(str(u.info) + str(u.desc))
    return session
'''

@app.route('/lfs/')
def lfs():
    show = "<pre>"
    for key in session:
        show += str(key) + ":" + str(session[key]) + "<br \\>"
    show += "</pre>"
    return show

@app.route('/lfu/<int:id>/')
def lfu(id):
    u = User(id)
    show = "<pre>"
    for attr in dir(u):
        if not attr.startswith("__"):
            value = getattr(u, attr)
            show += str(attr) + ":" + str(value) + "<br \\>"
    show += "</pre>"
    return show

@app.route('/lfd/<int:id>/')
def lfd(id):
    d = Discuss(id)
    show = "<pre>"
    for attr in dir(d):
        if not attr.startswith("__"):
            value = getattr(d, attr)
            show += str(attr) + ":" + str(value) + "<br \\>"
    show += "</pre>"
    return show


@app.route('/captcha/')
def captcha():
    # 使用上述函数生成验证码图片
    image, captcha_text = generate_captcha_image()

    # 将验证码文本存储到session，以便之后进行验证
    session['captcha'] = captcha_text

    buf = io.BytesIO()
    image.save(buf, format='PNG')
    buf.seek(0)
    return buf.getvalue(), 200, {
        'Content-Type': 'image/png',
        'Content-Length': str(len(buf.getvalue()))
    }


@app.route('/login/')
def login():
    if session['login']:
        return redirect('/')
    err = session.get('err')
    session['err'] = []
    if not err:
        err = []
    ran = random.randint(100, 999)
    session['ran'] = str(ran)
    return render_template("login.html", errors=err, ran=ran)


@app.route('/login/handle/', methods=['POST'])
def login_handle():
    username = flask.request.values.get('username')
    password = flask.request.values.get('password')
    captcha = flask.request.values.get('captcha')

    error1 = False
    error2 = False
    error3 = False  # 验证码
    c = get_cursor()
    c[1].execute(f"SELECT password FROM users WHERE username = ?", (username, ))
    data = c[1].fetchone()
    if data == None:
        error1 = True
    else:
        error2 = password != data[0]
    # 检查用户输入的验证码是否与session中的一致
    if captcha.upper() != session['captcha'].upper() and captcha != session['ran']:
        error3 = True
        session['login_times'] += 1
    if not error1 and not error2 and not error3:
        c[1].execute(f"SELECT * FROM users WHERE username = ?", (username, ))
        data = c[1].fetchall()[0]
        session['id'] = data[0]
        session['login'] = True
        session['username'] = data[1]
        session['admin'] = data[7]
        session['datas'] = data
        session.permanent = True
        session['login_times'] = 0
        c[0].commit()
        c[0].close()
        resp = make_response(redirect('/'))
        resp.set_cookie('user_id', str(c[0]), max_age=60 * 60 * 24 * 7)  # Cookie有效期为7天
        # return redirect("/")
        return resp
    else:
        session['err'] = []
        if error1:
            session['err'].append("用户不存在")
        elif error2:
            session['err'].append("用户名或密码错误")
        elif error3:
            session['err'].append("验证码输入错误")
        c[0].commit()
        c[0].close()
        return redirect("/login/")


@app.route('/login/logout/')
def logout():
    if not session['login']:
        return redirect('/login/')
    session['id'] = 0
    session['login'] = False
    session['username'] = None
    session['admin'] = False
    session['datas'] = None
    return redirect("/login/")


@app.route('/login/forgetpwd/')
def forgetpwd():
    if session['login']:
        return redirect('/')
    return render_template("login_fpwd.html", session=session)


@app.route("/login/forgetpwd/handle/", methods=['POST'])
def forgetpwd_handle():
    userid = request.form.get("id")
    rname = request.form.get("rname")
    eduid = request.form.get("eduid")
    pwd = request.form.get("pwd")
    s = dict()
    s['id'] = userid
    s['rname'] = rname
    s['eduid'] = eduid
    s['pwd'] = pwd
    forget_password_list.append(s)
    return render_template("success.html", session=session)
    # capt = request.form.get("capt")
    # if capt == session['capt_code']:
    #     return render_template("sucess.html", session=session)
    # else:
    #     return


# 暂时不用：发邮件验证码

@app.route('/login/forgetpwd/handle_c/', methods=['POST'])
def forgetpwd_handle_c():
    code = random.randint(100000, 999999)
    # email = request.form.get("email")
    # session['capt_code'] = code
    # html_content = render_template('email.html', token=code)
    #
    # message = Message(subject="班级圈-找回密码", recipients=[email], html=html_content)
    # # 添加图片附件
    # # with app.open_resource("static/img/logo.png") as fp:
    # #     message.attach("logo.png", "img/png", fp.read(), 'inline', headers=[['Content-ID', '<logo>']])
    # mail.send(message)
    return render_template("login_fpwd.html", session=session)#, email_=email)


# @app.route('/users/')
# def user():
#     dis = []
#     lsc = "Level " + str(session.get('datas')[4]) + " 积分" + str(session.get('datas')[5]) + " 活跃度" + str(session.get('datas')[6])
#     return render_template("users_me.html", session = session, tname = session.get('datas')[3], lvlsc = lsc, hedis = dis)

# @app.route('/users/<int:id>/')
# def users(id):
#     dis = []
#     dis_id = discuss_f(-1 if not session.get('login') else session.get('id'), id)
#     for did in dis_id:
#         dis.append(Discuss(did))
#     c = get_cursor()
#     c[1].execute(f"SELECT * FROM users WHERE id = '{id}'")
#     data = c[1].fetchone()
#     lsc = "Level " + str(data[4]) + " 积分" + str(data[5]) + " 活跃度" + str(data[6])
#     c[0].commit()
#     c[0].close()
#     picpath = "./../user/user_pic/{{ id }}."
#     return render_template("users.html", login = session.get('login'), username = data[1], admin = data[7], tname = data[3], lvlsc = lsc, hedis = dis)
# 

# @app.route('/discuss/list/')
# def discuss():
#     Ds = discuss_all_t()
#     logging.info(str(Ds))
#     return render_template("discuss.html", session = session, discuss = Ds)

# @app.route('/comment/new/', methods=['POST'])
# def new_comment():
#     if not session['login']:
#         return 'User not logged in', 401

#     data = request.get_json()
#     content = data.get('content')
#     parent_id = data.get('parent_id')

#     if not content or parent_id is None:
#         return 'Missing required parameters', 400

#     c = get_cursor()
#     c[1].execute("INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES (?, NULL, NULL, ?, ?, 'all', 0, 0)", (parent_id, get_time(), session['id']))
#     comment_id = c[1].lastrowid
#     c[0].commit()
#     c[0].close()

#     with open(f"./discuss/{comment_id}.txt", 'w', encoding='utf-8', newline = '\n') as f:
#         f.write(content)

#     return 'Comment submitted', 200


# @app.route('/comment/', methods=['POST'])
# def add_comment():
#     if not session.get('login'):
#         return jsonify({'error': 'User not logged in'}), 401

#     data = request.json
#     content = data.get('content')
#     parent_id = data.get('parent_id')
#     user_id = session['id']

#     if not content:
#         return jsonify({'error': 'Comment content is required'}), 400

#     c = get_cursor()
#     c[1].execute(f"INSERT INTO discuss (father, title, date, pub, csee, top, temp) VALUES ({parent_id}, '', '{get_time()}', {user_id}, 'all', 0, 0)")
#     comment_id = c[1].lastrowid
#     c[0].commit()
#     c[0].close()

#     with open(f"./discuss/{comment_id}.txt", 'w', encoding='utf-8', newline = '\n') as f:
#         f.write(content)

#     return jsonify({'success': True, 'comment_id': comment_id}), 201


# def get_comments(article_id):
#     c = get_cursor()
#     c[1].execute(f"SELECT * FROM discuss WHERE father = {article_id} AND temp = 0")
#     raw_comments = c[1].fetchall()
#     comments = []
#     for comment in raw_comments:
#         c[1].execute(f"SELECT username FROM users WHERE id = {comment[5]}")
#         user = c[1].fetchone()
#         if user is None:
#             username = '未知用户'
#         else:
#             username = user[0]
#         replies = get_comments(comment[0])  # 递归获取回复
#         comments.append({
#             "id": comment[0],
#             "content": render(open(f"./discuss/{comment[0]}.txt", 'r', encoding='utf-8').read()),
#             "username": username,
#             "replies": replies
#         })
#     c[0].commit()
#     c[0].close()
#     return comments

# @app.before_request
# def default_session():
#     if 'id' not in session:
#         session['id'] = 0
#     if 'login' not in session:
#         session['login'] = False
#     if 'admin' not in session:
#         session['admin'] = False

# fid = d.father
# if fid == None:
#     fid = 0
#     fname = ''
#     fname = ''
# else:
#     fname = Discuss(fid).title
# ptime = d.date
# subject = d.subject
# if subject:
#     subject = '无'
# cse = d.csee
# csc = d.csee_cnt
# toped = d.top
# pubid = d.pub_id
# c = get_cursor()
# # c[1].execute(f"SELECT * FROM users WHERE id = 'pubid'") #zhelishaolia{ /}
# dat = c[1].fetchone()
# pubname = dat[1]
# pubpic = dat[8]
# c[0].commit()
# c[0].close()
# title = d.title
# con = render(d.all_data)

@app.route('/discuss/<int:id>/')
def dicuss_detail(id):
    if not session['login']:
        return redirect('/login/')

    try:
        d = Discuss(id)
    except:
        return 'Discuss Not Found!', 404
    if d.temp:
        return redirect(f'/discuss/{id}/tmp')
    
    if d.csee != 'all' and str(session['id']) not in d.csee and session['id'] != d.pub_id and not session['admin']:
        return f'该讨论已屏蔽当前用户{session["username"]}', 404
    
    if d.father == 0:
        fid = 0
        fname = ""
    else:
        dtmp = Discuss(d.father)
        fid = dtmp.id
        fname = dtmp.title
    if d.subject:
        subject = d.subject.split(',')
    else:
        subject = ['无']
    # comments = get_comments(id)  # 获取评论和回复
    ta_list = d.find_sw_discuss(d.pub_id, id)
    comm1, comm2 = all_discuss(father=id, visiter=session['id'])
    comm2 = sorted(comm2, key=lambda s: s[4])
    comm2 = comm2[::-1]
    comments = []
    for it in comm1:
        comments.append(Discuss(it[0]))
    for it in comm2:
        comments.append(Discuss(it[0]))
    return render_template("discuss_detail.html", session=session,
                           id=d.id,
                           title=d.title,
                           pub_id=d.pub_id,
                           pub_truename=d.pub_truename,
                           pub_name=d.pub_name,
                           pub_pic=d.pub_pic,
                           father_id=fid,
                           father_name=fname,
                           pub_time=d.pub_time,
                           subjects=subject,
                           csee=d.csee,
                           csee_cnt=d.csee_cnt,
                           toped=d.top,
                           ta_list=ta_list,
                           content=render(d.all_data),
                           re_dis=comments)


@app.route('/discuss/<int:id>/reply/', methods=['GET'])
def discuss_reply_handle(id):
    content = request.args.get('reply_content', '评论内容')
    #logging.info("GET REPLY" + content)
    logging.info("REPLY FOR " + str(id) + " " + content)
    title = content
    father = id
    subject = '评论回复'
    zhiding = 0
    pub = session['id']
    csee = 'all'
    c = get_cursor()
    c[1].execute(
        f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (father, title, subject, get_time(), pub, csee, 0, 0))
    nowid = c[1].lastrowid
    c[0].commit()
    c[0].close()
    f = open(f"./discuss/{nowid}.txt", 'w', encoding='utf-8', newline = '\n')
    f.write(content)
    f.close()
    #try:
    #    add_new_post({'id': id, 'content': content})
    #except:
    #    set_search_tree()
    return redirect(f'/discuss/{id}/')


@app.route('/discuss/<int:id>/form_handle/<int:formid>/', methods=['GET', 'POST'])
def discuss_form_handle(id, formid):
    if not os.path.exists(f'./discussform/{id}/'):
        os.makedirs(f'./discussform/{id}/')
    if request.method == "GET":
        meth = "GET"
        tm = get_time()
        arg_txt = ""
        arg = request.args.to_dict()
        for k in arg:
            v = arg[k]
            arg_txt += f"{k}:{v},"
        arg_txt = arg_txt[:-1]
    elif request.method == "POST":
        meth = "POST"
        tm = get_time()
        arg_txt = ""
        arg = request.form.to_dict()
        print(arg)
        for k in arg:
            v = arg[k]
            arg_txt += f"{k}:{v},"
        arg_txt = arg_txt[:-1]
    else:
        meth = "UNKNOWN"
        tm = get_time()
        arg_txt = ""
    content = f"{meth} AT {tm} DATA [{arg_txt}]\n"
    f = open(f"./discussform/{id}/{formid}.txt", "a", encoding='utf-8', newline = '\n')
    f.write(content)
    f.close()
    return redirect(f'/discuss/{id}/')


@app.route('/discuss/<int:id>/csee/')
def discuss_detail_csee(id):
    # try:
    d = Discuss(id)
    # except:
    #    return "Discuss Not Found", 404
    if d.temp:
        return redirect(f'/discuss/{id}/tmp/csee')
    cse = d.csee
    if cse == 'all':
        cse = all_users()
    cse = cse.split(',')
    csee = []
    c = get_cursor()
    for cs in cse:
        if cs == 0:
            ls = [0, '游客', '0.PNG']
        else:
            c[1].execute(f"SELECT * FROM users WHERE id = ?", (cs, ))
            dat = c[1].fetchone()
            if dat != None:
                ls = [cs, dat[1], dat[8]]
                csee.append(ls)
    c[0].commit()
    c[0].close()
    return render_template("discuss_detail_csee.html", session=session, csee=csee)


@app.route('/discuss/<int:id>/tmp/')
def discuss_detail_tmp(id):
    if not session['login']:
        return redirect('/login/')
    # try:
    d = Discuss(id)
    # except:
    #    return "Discuss Not Found", 404
    if not d.temp:
        return redirect(f'/discuss/{id}')
    seer = User(session['id'])
    if not seer.admin and seer.id != d.pub_id:
        return '你没有查看该临时帖子的权限'
    if d.father == 0:
        fid = 0
        fname = ""
    else:
        dtmp = Discuss(d.father)
        fid = dtmp.id
        fname = dtmp.title
    '''
    fid = d.father
    if fid == None:
        fid = 0
        fname = ''
    else:
        fname = Discuss(fid).title
    ptime = d.date
    subject = d.subject
    if subject:
        subject = '无'
    cse = d.csee
    csc = d.csee_cnt
    toped = d.top
    pubid = d.pub_id
    c = get_cursor()
    c[1].execute(f"SELECT * FROM users WHERE id = '{pubid}'")
    dat = c[1].fetchone()
    pubname = dat[1]
    pubpic = dat[8]
    c[0].commit()
    c[0].close()
    title = d.title
    con = render(d.all_data)
    '''
    return render_template("discuss_detail_tmp.html", session=session,
                           title=d.title,
                           pub_id=d.pub_id,
                           pub_name=d.pub_name,
                           pub_pic=d.pub_pic,
                           father_id=d.father,
                           father_name=fid,
                           pub_time=fname,
                           subjects=d.subject,
                           csee=d.csee,
                           csee_cnt=d.csee_cnt,
                           toped=d.top,
                           content=render(d.all_data), 
                           selfid = id
                           )


@app.route('/discuss/<int:id>/tmp/handle/accept/', methods=["POST"])
def discuss_detail_tmp_handle1(id):
    if not session['login']:
        return redirect('/login/')
    # try:
    d = Discuss(id)
    # except:
    #    return "Discuss Not Found", 404
    if not d.temp:
        return "Discuss Not Found", 404
    seer = User(session['id'])
    if not seer.admin:
        return '你没有查看该临时帖子的权限'
    d.temp = 0
    d.save(None)
    f = open('./templist.txt', 'r', encoding='utf-8')
    dat = f.read()
    f.close()
    ls = dat.split(',')
    nls = []
    for ele in ls:
        if ele != str(id):
            nls.append(ele)
    dat = ','.join(nls)
    f = open("./templist.txt", 'w', encoding='utf-8', newline = '\n')
    f.write(dat)
    f.close()
    #dsearch.add_search_tree(d)
    return redirect(f"/discuss/{id}/")
    #return "alert('帖子审核成功！访问链接：" + f'/discuss/{id}' + "')"


@app.route('/discuss/<int:id>/tmp/handle/reject/', methods=["POST"])
def discuss_detail_tmp_handle2(id):
    if not session['login']:
        return redirect('/login/')
    # try:
    d = Discuss(id)
    # except:
    #    return "Discuss Not Found", 404
    if not d.temp:
        return "Discuss Not Found", 404
    seer = User(session['id'])
    if not seer.admin:
        return '你没有查看该临时帖子的权限'
    d.temp = 1
    d.save(None)
    return redirect(f"/discuss/{id}/tmp/")


@app.route('/discuss/<int:id>/tmp/handle/delete/', methods=["POST"])
def discuss_detail_tmp_handle3(id):
    if not session['login']:
        return redirect('/login/')
    # try:
    d = Discuss(id)
    # except:
    #    return "Discuss Not Found", 404
    if not d.temp:
        return "Discuss Not Found", 404
    seer = User(session['id'])
    if not seer.admin:
        return '你没有查看该临时帖子的权限'
    c = get_cursor()
    c[1].execute(f"DELETE FROM discuss WHERE id = ?;", (id, ))
    c[0].commit()
    c[0].close()
    f = open('./templist.txt', 'r', encoding='utf-8')
    dat = f.read()
    f.close()
    ls = dat.split(',')
    nls = []
    for ele in ls:
        if ele != str(id):
            nls.append(ele)
    dat = ','.join(nls)
    f = open("./templist.txt", 'w', encoding='utf-8', newline = '\n')
    f.write(dat)
    f.close()
    return redirect("/discuss/list/")


@app.route('/discuss/<int:id>/tmp/csee/')
def discuss_detail_tmp_csee(id):
    if not session['login']:
        return redirect('/login/')
    # try:
    d = Discuss(id)
    # except:
    #    return "Discuss Not Found", 404
    if not d.temp:
        return redirect(f'/discuss/{id}/csee')
    seer = User(session['id'])
    if not seer.admin and seer.id != d.pub_id:
        return '你没有查看该临时帖子的权限'
    cse = d.csee
    if cse == 'all':
        cse = all_users()
    cse = cse.split(',')
    csee = []
    c = get_cursor()
    for cs in cse:
        if cs == 0:
            ls = [0, '游客', '0.PNG']
        else:
            c[1].execute(f"SELECT * FROM users WHERE id = ?", (cs, ))
            dat = c[1].fetchone()
            if dat != None:
                ls = [cs, dat[1], dat[8]]
                csee.append(ls)
    c[0].commit()
    c[0].close()
    return render_template("discuss_detail_tmp_csee.html", session=session, csee=csee)


@app.route('/discuss/new/')
def discuss_new():
    if not session['login']:
        return redirect('/login/')
    fid = request.args.get('fid')
    cs = request.args.get('cs')
    return render_template("discuss_new.html", session=session, fid=fid, cs=cs)


'''
@app.route('/discuss/new_notitle/')
def discuss_new_notitle():
    if not session['login'] or session['id'] == 0:
        return redirect('/login/')
    fid = request.args.get('fid')
    return render_template("discuss_new_notitle.html", session=session, fid=fid)


@app.route('/discuss/new_file/')
def discuss_new_file():
    if not session['login']:
        return redirect('/login/')
    fid = request.args.get('fid')
    return render_template("discuss_new_file.html", session=session, fid=fid)
'''


@app.route('/discuss/new/handle/save/', methods=['POST'])
def discuss_new_handle1():
    if not session['login']:
        return redirect('/login/')
    data = flask.request.get_json()
    title = data.get('title')
    if title == '':
        title = '[无标题]'
    father = data.get('father')
    subject = data.get('subject')
    zhiding = data.get('zhiding')
    pub = session['id']
    csee = data.get('csee')
    content = data.get('text')
    c = get_cursor()
    if csee == '':
        csee = 'all'
    if father != '':
        father = int(father)
        # logging.info(
        #     f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES ({father}, {title}, {subject}, {get_time()}, {pub}, {csee}, 0, 1)")
        # c[1].execute(
        #     f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES ({father}, '{title}', '{subject}', '{get_time()}', {pub}, '{csee}', 0, 1)")
    else:
        father = 0
        # logging.info(
        #     f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES ({-1}, {title}, {subject}, {get_time()}, {pub}, {csee}, 0, 1)")
        # c[1].execute(
        #     f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES (0, '{title}', '{subject}', '{get_time()}', {pub}, '{csee}', 0, 1):)
    if zhiding == '1':
        c[1].execute(
            f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (father, title, subject, get_time(), pub, csee, 1, 1))
    else:
        c[1].execute(
            f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (father, title, subject, get_time(), pub, csee, 0, 1))
    nowid = c[1].lastrowid
    c[0].commit()
    c[0].close()
    f = open(f"./discuss/{nowid}.txt", 'w', encoding='utf-8', newline = '\n')
    logging.info(f"Write to ./discuss/{nowid}.txt : {content}")
    f.write(content)
    f.close()
    return f"/discuss/edit/{nowid}/"


@app.route('/discuss/new/handle/render/', methods=['POST'])
def discuss_new_handle2():
    if not session['login']:
        return redirect('/login/')
    data = flask.request.get_json()
    title = data.get('title')
    if title == '':
        title = '[无标题]'
    father = data.get('father')
    subject = data.get('subject')
    zhiding = data.get('zhiding')
    # logging.info(f"================================{zhiding}================================")
    pub = session['id']
    csee = data.get('csee')
    content = data.get('text')
    c = get_cursor()
    if csee == '':
        csee = 'all'
    if father != '':
        father = int(father)
    else:
        father = 0
    # logging.info(zhiding, type(zhiding))
    if zhiding == '1':
        logging.info(
            f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES ({father}, {title}, {subject}, {get_time()}, {pub}, {csee}, 1, 1)")
        c[1].execute(
            f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (father, title, subject, get_time(), pub, csee, 1, 1))
    else:
        logging.info(
            f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES ({father}, {title}, {subject}, {get_time()}, {pub}, {csee}, 0, 1)")
        c[1].execute(
            f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (father, title, subject, get_time(), pub, csee, 0, 1))
    nowid = c[1].lastrowid
    c[0].commit()
    c[0].close()
    f = open(f"./discuss/{nowid}.txt", 'w', encoding='utf-8', newline = '\n')
    f.write(content)
    f.close()
    return f"/discuss/{nowid}/tmp/"


@app.route('/discuss/new/handle/publish/', methods=['POST'])
def discuss_new_handle3():
    if not session['login']:
        return redirect('/login/')
    data = flask.request.get_json()
    title = data.get('title')
    if title == '':
        title = '[无标题]'
    father = data.get('father')
    subject = data.get('subject')
    zhiding = data.get('zhiding')
    # logging.info(f"================================{zhiding}================================")
    pub = session['id']
    csee = data.get('csee')
    content = data.get('text')
    c = get_cursor()
    if csee == '':
        csee = 'all'
    if father != '':
        father = int(father)
    else:
        father = 0
    if zhiding == '1':
        logging.info(
            f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES ({father}, {title}, {subject}, {get_time()}, {pub}, {csee}, 1, 1)")
        c[1].execute(
            f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (father, title, subject, get_time(), pub, csee, 1, 1))
    else:
        logging.info(
            f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES ({father}, {title}, {subject}, {get_time()}, {pub}, {csee}, 0, 1)")
        c[1].execute(
            f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (father, title, subject, get_time(), pub, csee, 0, 1))
    nowid = c[1].lastrowid
    c[0].commit()
    c[0].close()
    f = open(f"./discuss/{nowid}.txt", 'w', encoding='utf-8', newline = '\n')
    f.write(content)
    f.close()
    f = open("./templist.txt", 'a', encoding='utf-8')
    f.write(',' + str(nowid))
    f.close()
    '''
    try:
        add_search_tree(Discuss(id))
        add_new_post({'id': id, 'content': content})
    except:
        pass
    '''
    return f"/discuss/{nowid}/tmp/"


@app.route('/discuss/edit/<int:id>/')
def discuss_edit(id):
    if not session['login']:
        return redirect('/login/')
    # try:
    d = Discuss(id)
    # except:
    #    return "Discuss Not Found", 404
    seer = User(session['id'])
    if not seer.admin and seer.id != d.pub_id:
        return '你没有修改该临时帖子的权限'
    fid = d.father
    if fid == None or fid == 0:
        fid = 0
        fname = ""
    else:
        fname = Discuss(fid).title
    subject = d.subject
    if not subject:
        subject = '无'
    return render_template("discuss_edit.html", session=session,
                           title=d.title,
                           fid=fid,
                           subject=subject,
                           csee=d.csee,
                           content=d.all_data
                           )


@app.route('/discuss/edit/<int:id>/handle/save/', methods=['POST'])
def discuss_edit_handle1(id):
    seer = User(session['id'])
    dis = Discuss(id)
    if not seer.admin and seer.id != dis.pub_id:
        return '你没有修改该临时帖子的权限'
    holdname = True
    if dis.pub_id != seer.id:
        f = open("./data/edit_hold_publisher.txt", "r", encoding = 'utf-8')
        ch = f.read()
        f.close()
        holdname = (ch == 'T')
    data = flask.request.get_json()
    title = data.get('title')
    father = data.get('father')
    subject = data.get('subject')
    if not holdname:
        pub = session['id']
    else:
        pub = dis.pub_id
    csee = data.get('csee')
    content = data.get('text')
    c = get_cursor()
    if csee == '':
        csee = 'all'
    logging.info(
        f"UPDATE discuss SET title = '{title}', subject = '{subject}', date = '{get_time()}', pub = {pub}, csee = '{csee}', top = 0, temp = 1 WHERE id = {id}")
    c[1].execute(
        f"UPDATE discuss SET title = '{title}', subject = '{subject}', date = '{get_time()}', pub = {pub}, csee = '{csee}', top = 0, temp = 1 WHERE id = ?", (id, ))
    c[0].commit()
    c[0].close()
    f = open(f"./discuss/{id}.txt", 'w', encoding='utf-8', newline = '\n')
    logging.info(f"Write to ./discuss/{id}.txt : {content}")
    f.write(content)
    f.close()
    return f"/discuss/edit/{id}"


@app.route('/discuss/edit/<int:id>/handle/render/', methods=['POST'])
def discuss_edit_handle2(id):
    seer = User(session['id'])
    dis = Discuss(id)
    if not seer.admin and seer.id != dis.pub_id:
        return '你没有修改该临时帖子的权限'
    holdname = True
    if dis.pub_id != seer.id:
        f = open("./data/edit_hold_publisher.txt", "r", encoding = 'utf-8')
        ch = f.read()
        f.close()
        holdname = (ch == 'T')
    data = flask.request.get_json()
    title = data.get('title')
    father = data.get('father')
    subject = data.get('subject')
    if not holdname:
        pub = session['id']
    else:
        pub = dis.pub_id
    csee = data.get('csee')
    content = data.get('text')
    c = get_cursor()
    if csee == '':
        csee = 'all'
    logging.info(
        f"UPDATE discuss SET title = '{title}', subject = '{subject}', date = '{get_time()}', pub = {pub}, csee = '{csee}', top = 0, temp = 1 WHERE id = {id}")
    c[1].execute(
        f"UPDATE discuss SET title = ?, subject = ?, date = ?, pub = ?, csee = ?, top = ?, temp = ? WHERE id = ?", (title, subject, get_time(), pub, csee, 0, 1, id))
    c[0].commit()
    c[0].close()
    f = open(f"./discuss/{id}.txt", 'w', encoding='utf-8', newline = '\n')
    f.write(content)
    f.close()
    return f"/discuss/{id}/tmp"


@app.route('/discuss/edit/<int:id>/handle/publish/', methods=['POST'])
def discuss_edit_handle3(id):
    seer = User(session['id'])
    dis = Discuss(id)
    if not seer.admin and seer.id != dis.pub_id:
        return '你没有修改该临时帖子的权限'
    holdname = True
    if dis.pub_id != seer.id:
        f = open("./data/edit_hold_publisher.txt", "r", encoding = 'utf-8')
        ch = f.read()
        f.close()
        holdname = (ch == 'T')
    data = flask.request.get_json()
    title = data.get('title')
    father = data.get('father')
    subject = data.get('subject')
    if not holdname:
        pub = session['id']
    else:
        pub = dis.pub_id
    csee = data.get('csee')
    content = data.get('text')
    c = get_cursor()
    if csee == '':
        csee = 'all'
    logging.info(
        f"UPDATE discuss SET title = '{title}', subject = '{subject}', date = '{get_time()}', pub = {pub}, csee = '{csee}', top = 0, temp = 1 WHERE id = {id}")
    c[1].execute(
        f"UPDATE discuss SET title = ?, subject = ?, date = ?, pub = ?, csee = ?, top = ?, temp = ? WHERE id = ?", (title, subject, get_time(), pub, csee, 0, 1, id))
    c[0].commit()
    c[0].close()
    f = open(f"./discuss/{id}.txt", 'w', encoding='utf-8', newline = '\n')
    f.write(content)
    f.close()
    f = open("./templist.txt", 'a', encoding='utf-8')
    f.write(',' + str(id))
    f.close()
    # add_search_tree(Discuss(id))
    # set_search_tree()

    add_search_tree(Discuss(id))
    add_new_post({'id': id, 'content': content})

    return redirect(f'/discuss/{id}/')

@app.route('/discuss/smbox/')
def smbox_all():
    if not session['login']:
        return redirect('/login/')
    mess = get_sm(session['id'], None)
    print("GET MESS", len(mess))
    for d in mess:
        print(d.id)
    return render_template("smbox_all.html", session=session, messages = mess)

@app.route('/discuss/smbox/<int:id>/')
def smbox_one(id):
    if not session['login']:
        return redirect('/login/')
    mess = get_sm(session['id'], id)
    print("GET MESS", len(mess))
    for d in mess:
        print(d.id)
    return render_template("smbox_one.html", session=session, ou = User(id), messages = mess)

@app.route('/discuss/smbox/new/')
def smbox_new():
    arg = request.args.to_dict()
    content = arg['content']
    listeners = arg['recv']
    title = '[私信]'
    father = 0
    subject = '私信'
    zhiding = 0
    pub = session['id']
    csee = listeners
    #print(f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES (father, title, subject, {get_time()}, {pub}, {csee}, 0, 0)")
    c = get_cursor()
    c[1].execute(
        f"INSERT INTO discuss (father, title, subject, date, pub, csee, top, temp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (father, title, subject, get_time(), pub, csee, 0, 0))
    nowid = c[1].lastrowid
    c[0].commit()
    c[0].close()
    f = open(f"./discuss/{nowid}.txt", 'w', encoding='utf-8', newline = '\n')
    f.write(content)
    f.close()
    return redirect('/discuss/smbox/')

@app.route('/discuss/pic_upload/')
def pic_upload():
    if not session['login']:
        return redirect('/login/')
    return render_template("discuss_pic_upload.html", session=session)


@app.route('/discuss/pic_handle/', methods=['POST'])
def pic_handle():
    if not session['login']:
        return redirect('/login/')

    if 'file' not in request.files:
        return '上传失败'

    file = request.files['file']
    if file.filename == '':
        return '上传失败'

    if file:
        f = open("./static/discuss_img/file_cnt.txt", 'r')
        dat = int(f.read()) + 1
        f.close()
        f = open("./static/discuss_img/file_cnt.txt", 'w', newline = '\n')
        f.write(str(dat))
        f.close()
        filepath = str(dat) + os.path.splitext(file.filename)[1]
        file.save(os.path.join('./static/discuss_img/', filepath))
        return render_template("discuss_pic_upload.html", session=session, postad=filepath)
    else:
        return '上传失败'


@app.route('/discuss/file_upload/')
def file_upload():
    if not session['login']:
        return redirect('/login/')
    return render_template("discuss_file_upload.html", session=session)


@app.route('/discuss/file_handle/', methods=['POST'])
def file_handle():
    if not session['login']:
        return redirect('/login/')

    if 'file' not in request.files:
        return '上传失败'

    file = request.files['file']
    if file.filename == '':
        return '上传失败'

    if file:
        f = open("./static/discuss_file/file_cnt.txt", 'r')
        dat = int(f.read()) + 1
        f.close()
        f = open("./static/discuss_file/file_cnt.txt", 'w', newline = '\n')
        f.write(str(dat))
        f.close()
        filepath = str(dat) + os.path.splitext(file.filename)[1]
        file.save(os.path.join('./static/discuss_file/', filepath))
        return render_template("discuss_file_upload.html", session=session, postad=filepath)
    else:
        return '上传失败'


'''
@app.route('/search/')
def search():
    rsearch = request.form.get('resource_search', '')
    gettypes = request.form.get('cb', '2,3')
    sortways = request.form.get('sw', 'a')
    logging.info("Log To Console : " + str(rsearch) + str(gettypes) + str(sortways))
    return render_template("search.html", session = session, rsearch = rsearch, cw = gettypes, sw = sortways)
    # prs = rsearch, sc = gettypes, ff = sortways
'''


@app.route('/discuss/list/')
def discuss_search():
    # session['id'] = 0
    rsearch = request.args.get('resource_search', '')
    ar = request.values.getlist("diff")
    if ar == []:
        okdiff = "OFF"
    else:
        okdiff = ar[0]
    if okdiff == "OFF":
        fr1, fr2 = all_discuss(None, None, session['id'])
        ft1 = []
        ft2 = []
        for it in fr1:
            if rsearch in it[2] or (it[3] and subject_search(it[3], rsearch)):
                ft1.append(it)
        for it in fr2:
            if rsearch in it[2] or (it[3] and subject_search(it[3], rsearch)):
                ft2.append(it)
        ft2 = sorted(ft2, key=lambda s: s[4])
        ft2 = ft2[::-1]
        fg = []
        for it in ft1:
            fg.append(Discuss(it[0]))
        for it in ft2:
            fg.append(Discuss(it[0]))
        res = fg
    else:
        fg = []
        [fg.append(i) for i in complex_search(rsearch)]
        ff = []
        [ff.append(i) for i in fg if i not in ff]
        res = ff
    res = [i for i in res if '私信' not in i.subject]
    res = [i for i in res if '评论回复' not in i.subject]
    return render_template("discuss_list.html", session=session, rsearch=rsearch, dis=res)


@app.route('/resource/<int:id>/')
def resource_detail(id):
    if not session['login']:
        return redirect('/login/')
    try:
        d = Resource(id)
    except:
        return 'Resource Not Found!', 404

    fid = 0
    fname = ""
    if d.subject:
        subject = d.subject.split(',')
    else:
        subject = ['无']
    return render_template("resource_detail.html", session=session,
                           id=d.id,
                           title=d.title,
                           pub_id=d.pub_id,
                           pub_truename=d.pub_truename,
                           pub_name=d.pub_name,
                           pub_pic=d.pub_pic,
                           father_id=fid,
                           father_name=fname,
                           pub_time=d.pub_time,
                           subjects=subject,
                           csee='all',
                           csee_cnt=user_cnt(),
                           toped=0,
                           content=render(d.all_data),
                           )


@app.route('/resource/list/')
def resource_search():
    rsearch = request.args.get('resource_search', '')
    fr1, fr2 = all_resource(None)
    ft2 = []
    for it in fr2:
        if rsearch in it[2] or (it[3] and subject_search(it[3], rsearch)):
            ft2.append(it)
    ft2 = sorted(ft2, key=lambda s: s[4])
    ft2 = ft2[::-1]
    fg = []
    for it in ft2:
        fg.append(Resource(it[0]))
    return render_template("resource_list.html", session=session, rsearch=rsearch, dis=fg)


@app.route('/activity/')
def activity():
    f = open('./data/activity.txt', 'r', encoding='utf-8')
    con = f.read()
    f.close()
    con = con.split('\n')
    idx = 5
    activity_list = []
    for i in con:
        t = i.split(':')
        if idx <= 9:
            t.append('0' + str(idx))
        else:
            t.append(str(idx))
        activity_list.append(t)
        idx += 1
    return render_template("activity.html", session=session, activity_list=activity_list)


@app.route('/activity/<int:id>/')
def activity_list(id):
    f = open(f'./data/activity/{id}.txt', 'r', encoding='utf-8')
    con = f.read()
    logging.info(con)
    f.close()
    con = con.split('\n')
    logging.info(con)
    idx = 1
    activity_list = []
    for i in con:
        logging.info(i)
        t = i.split(':')
        t.append(str(idx))
        t.append(render(get_discuss(int(t[1]))))
        logging.info(t)
        activity_list.append(t)
        idx += 1
    logging.info(activity_list)
    return render_template("activity_shell.html", session=session, activity_list=activity_list)


@app.route('/activity/learn/')
def learn():
    return render_template("learn.html", session=session)


@app.route('/activity/learn/<int:nid>/')
def learn_shell(nid):  # nid从0开始
    # items每项是列表，第0项是item-20xx_xx，第1项是“20xx年第x期”，第2项是discuss content
    f = open('./data/learn.txt', 'r', encoding='utf-8')
    content = f.read().split('>\n')
    f.close()
    content = [i for i in content if i != ""]
    subject = content[nid]
    subject = subject.split('\n')
    items = []
    for i in subject:
        if i == '':
            continue
        item = i.split(':')
        ic = item[0]
        l = item[0].split('_')
        wd = l[0] + '年第' + str(int(l[1])) + '期'
        fd = open(f'./discuss/{item[1]}.txt', 'r', encoding="utf-8")
        ct = fd.read()
        ct = render(ct, learn=True)
        fd.close()
        items.append([ic, wd, ct])
    return render_template("learn_shell.html", session=session, items=items)


@app.route('/resource/')
def resource():
    return redirect('/resource/list/')


@app.route('/album/')
def album():
    # album_dir = {'begin': '开学', 'books': '读书活动', 'comparison': '竞选', 'confucius': '孔子的故事',
    #              'method': '学习方法', 'military': '军训', 'newyear': '新年', 'sport': '运动会',
    #              'sudongpo': '苏东坡活动', 'travel': '游学', 'other': '其他', 'debate': '辩论',
    #              'play': '休闲'}  # 'debate':'辩论',
    # album_dict = {'begin': 1, 'books': 2, 'comparison': 3, 'confucius': 4, 'method': 6, 'military': 7, 'newyear': 8,
    #               'sport': 9, 'sudongpo': 10, 'travel': 11, 'other': 12, 'debate': 5, 'play': 13}  # 'debate':5,
    #
    # with shelve.open('album') as db:
    #
    album_dir = {}
    album_dict = {}
    f = open("./data/album.txt", "r", encoding='utf-8')
    rk = f.readlines()
    f.close()
    for al in rk:
        if al.endswith('\n'):
            al = al[:-1]
        nms = al.split('*')
        album_dir[nms[0]] = nms[1]
        album_dict[nms[0]] = int(nms[2])
    '''
    with shelve.open('dsearch') as db:
        album_dir = db['album_dir']
        album_dict = db['album_dict']
    '''
    return render_template('album.html', session=session, album_dir=album_dir, album_dict=album_dict)


@app.route('/album/<int:id>/')
def album_detail(id):
    # album_dir = {'begin':'开学', 'books':'读书活动', 'comparison':'竞选', 'confucius':'孔子的故事', 'debate':'辩论', 'method':'学习方法', 'military':'军训', 'newyear':'新年', 'sport':'运动会', 'sudongpo':'苏东坡活动', 'travel':'游学', 'other':'其他'}
    # album_dict = {'begin':1, 'books':2, 'comparison':3, 'confucius':4, 'debate':5, 'method':6, 'military':7, 'newyear':8, 'sport':9, 'sudongpo':10, 'travel':11, 'other':12}
    # album_list = []
    # for key in album_dir.keys():
    #     image_folder = os.path.join('static', 'album', key)
    #     #image_folder = os.path.join('static', 'img')
    #     images = os.listdir(image_folder)
    #     #images = ['album/' + key + '/' + image for image in images if image.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    #     images = [image for image in images if image.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    #     #images = ['img/' + image for image in images if image.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    #     image_folder = os.path.join('static', 'album')
    
    
    
    if not session['login']:
        return redirect('/login/')
    
    sm_w = []
    sm_s = []
    sm_h = []
    bg_w = []
    bg_s = []
    bg_h = []
    '''
    bg_s * 2 -> 1:1 ph147456 cp921600
    bg_w * 1 -> 16:9 ph331776 cp2073600
    bg_h * 3 -> 9:16 ph116508 cp728177

    sm_s * 4 -> 1:1 ph36864 cp230400
    sm_w * 3 -> 16:9 ph36864 cp230400
    sm_h * 5 -> 9:16 ph41943 cp262144
    '''
    imf = os.listdir(f"./static/album/{id}/")
    for i in imf:
        path = f'./static/album/{id}/{i}'
        try:
            ida = numpy.fromfile(path, dtype=numpy.uint8)
            img = cv2.imdecode(ida, cv2.IMREAD_COLOR)
            # img = cv2.imread(path)
            height, width, channels = img.shape
        except:
            continue
        logging.info("图片尺寸：" + str(width) + "x" + str(height))
        if abs(width - height) < (width + height) * 0.15:
            if width * height > 100000:
                bg_s.append(i)
            else:
                sm_s.append(i)
        elif width > height:  # height > width:#
            #logging.info(str(i) + 'go to width with' + str(width) + str(height))
            if width * height > 300000:
                bg_w.append(i)
            else:
                sm_w.append(i)
        elif height > width:  # width > height:#
            if width * height > 80000:
                bg_h.append(i)
            else:
                sm_h.append(i)
    random.shuffle(sm_w)
    random.shuffle(sm_s)
    random.shuffle(sm_h)
    random.shuffle(bg_w)
    random.shuffle(bg_s)
    random.shuffle(bg_h)
    sm_w = sm_w[:len(sm_w) // 3 * 3]
    sm_s = sm_s[:len(sm_s) // 4 * 4]
    sm_h = sm_h[:len(sm_h) // 5 * 5]
    bg_w = bg_w[:len(bg_w) // 1 * 1]
    bg_s = bg_s[:len(bg_s) // 2 * 2]
    bg_h = bg_h[:len(bg_h) // 3 * 3]
    img_tp = []
    for i in range(len(sm_w) // 3):
        img_tp.append(1)
    for i in range(len(sm_s) // 4):
        img_tp.append(2)
    for i in range(len(sm_h) // 5):
        img_tp.append(3)
    for i in range(len(bg_w) // 1):
        img_tp.append(4)
    for i in range(len(bg_s) // 2):
        img_tp.append(5)
    for i in range(len(bg_h) // 3):
        img_tp.append(6)
    random.shuffle(img_tp)
    res = ""
    for k in img_tp:
        res += '\n<div class = "ot row" style = "margin: 0px; padding: 0px; width: 100%;">'
        if k == 1:
            for i in range(3):
                res += f'\n<div class = "in col rdiv spack col" style = "padding-left: 0px;">\n<img src = "../../static/album/{id}/{sm_w.pop()}" class = "wpic" />\n</div>'
        elif k == 2:
            for i in range(4):
                res += f'\n<div class = "in col rdiv spack col" style = "padding-left: 0px;">\n<img src = "../../static/album/{id}/{sm_s.pop()}" class = "spic" />\n</div>'
        elif k == 3:
            for i in range(5):
                res += f'\n<div class = "in col rdiv spack col" style = "padding-left: 0px;">\n<img src = "../../static/album/{id}/{sm_h.pop()}" class = "hpic" />\n</div>'
        elif k == 4:
            for i in range(1):
                res += f'\n<div class = "in col rdiv spack col" style = "padding-left: 0px;">\n<img src = "../../static/album/{id}/{bg_w.pop()}" class = "wpic" />\n</div>'
        elif k == 5:
            for i in range(2):
                res += f'\n<div class = "in col rdiv spack col" style = "padding-left: 0px;">\n<img src = "../../static/album/{id}/{bg_s.pop()}" class = "spic" />\n</div>'
        elif k == 6:
            for i in range(3):
                res += f'\n<div class = "in col rdiv spack col" style = "padding-left: 0px;">\n<img src = "../../static/album/{id}/{bg_h.pop()}" class = "hpic" />\n</div>'
        res += '\n</div>'
    res = res[1:]
    return render_template('album_detail_shell.html', session=session, content=res)

@app.route('/album/video/')
def album_detail_video():
    if not session['login']:
        return redirect('/login/')
    path = f'../../static/album/uua/{random.choice(os.listdir(f"./static/album/uua/"))}'
    res = f'<div class = "ot row" style = "margin: 0px; padding: 0px; width: 100%;"><div class = "in col rdiv spack col" style = "padding-left: 0px;"><video width="100%" controls><source src="{path}"">视频</source></video></div></div>'
    return render_template('album_detail_shell.html', session=session, content=res)

@app.route('/setting/pic_upload/')
def album_upload():
    if not session['login']:
        return redirect('/login/')
    return render_template("discuss_album_upload.html", session=session)


@app.route('/setting/pic_handle/', methods=['POST'])
def album_handle():
    if not session['login']:
        return redirect('/login/')
    #'''
    if not session.get('admin'):
        return redirect('/')
    #'''

    if 'file' not in request.files:
        return '上传失败'

    file = request.files['file']
    if file.filename == '':
        return '上传失败'


    if file:
        fq = request.form['type']
        filepath = randstr() + os.path.splitext(file.filename)[1]
        if fq == 'video':
            fullfp = os.path.join('./static/album/uua/', filepath)
        else:
            fullfp = os.path.join(f'./static/album/{fq}/', filepath)
        file.save(fullfp)
        return render_template("discuss_album_upload.html", session=session, postad = 1)


@app.route('/setting/pic_folder_handle/', methods=['POST'])
def album_folder_handle():
    if not session['login']:
        return redirect('/login/')
    #'''
    if not session.get('admin'):
        return redirect('/')
    '''
    file = request.files['file']
    if file.filename == '':
        return '上传失败'
    '''
    fq = request.form['type']
    wz = request.form['type_name']
    en = request.form['type_en_name']
    # filepath = randstr() + os.path.splitext(file.filename)[1]
    # if fq == 'video':
    #     fullfp = os.path.join('./static/album/uua/', filepath)
    #else:
    fullfp = f'./static/album/{fq}/'
    if not os.path.exists(fullfp):
        os.mkdir(fullfp)
    # album_dir = {'begin': '开学', 'books': '读书活动', 'comparison': '竞选', 'confucius': '孔子的故事',
    #              'method': '学习方法', 'military': '军训', 'newyear': '新年', 'sport': '运动会',
    #              'sudongpo': '苏东坡活动', 'travel': '游学', 'other': '其他', 'debate': '辩论',
    #              'play': '休闲'}  # 'debate':'辩论',
    # album_dict = {'begin': 1, 'books': 2, 'comparison': 3, 'confucius': 4, 'method': 6, 'military': 7, 'newyear': 8,
    #               'sport': 9, 'sudongpo': 10, 'travel': 11, 'other': 12, 'debate': 5, 'play': 13}  # 'debate':5,
    #
    # with shelve.open('album') as db:
    #
    f = open("./data/album.txt", "a", encoding='utf-8', newline = '\n')
    f.write(en + "*" + wz + "*" + fq + "\n")
    f.close()
    '''
    with shelve.open('album') as db:
        album_dir = db['album_dir']
        album_dict = db['album_dict']
        album_dict[en] = fq
        album_dir[en] = wz
        db['album_dir'] = album_dir
        db['album_dict'] = album_dict
    '''
    return render_template("discuss_album_upload.html", session=session, postad = 1)


@app.route('/forum/')
def forum():
    return redirect('/discuss/list/')


# 暂且先如此处理
@app.route('/information/')
def information():
    return render_template("information.html", session=session)


'''
@app.route('/information/<string:path>/')
def information(path):
    f = open("./info/filename.txt")
    kk = f.readlines()
    f.close()
    ls = []
    for k in kk:
        ls.append(k.split(' '))
    f = open(f"./info/{path.replace('-', '/')}.txt")
    cc = f.readlines()
    f.close()
    try:
        title = cc[0]
    except:
        title = "无标题班规"
    cc = '<br>'.join(cc)
    return render_template("information_shell.html", session = session, ls = ls, title = title, content = cc)
@app.route('/docs/<string:path>/')
def information_docs(path):
    f = open("./info/filename.txt")
    kk = f.readlines()
    f.close()
    ls = []
    for k in kk:
        ls.append(k.split(' '))
    f = open(f"./info/docs/{path.replace('-', '/')}.txt")
    cc = f.readlines()
    f.close()
    try:
        title = cc[0]
    except:
        title = "无标题"
    cc = '<br>'.join(cc[1:])
    return render_template("information_shell.html", session = session, ls = ls, title = title, content = cc)
'''


@app.route("/user/me/")
def user_me():
    if not session['login']:
        return redirect('/login/')
    u = User(session['id'])
    if u.id == -1:
        return redirect('/login/logout/')
    dl = get_user_discuss(u.id)
    return render_template("user_me.html", user=u, session=session, discuss_list=dl)


@app.route("/user/<int:id>/")
def user(id):
    if id == session['id']:
        return redirect('../me/')
    u = User(id)
    dl = get_user_discuss(u.id)
    return render_template("user.html", user=u, session=session, discuss_list=dl)

@app.route("/user/<int:id>/discuss/")
def user_discuss(id):
    u = User(id)
    dl = get_user_discuss(u.id, False)
    dl2 = get_user_discuss2(u.id)
    return render_template("user_discuss.html", user=u, session=session, sh1=dl, sh2=dl2)

@app.route("/user/<int:id>/fix/")
def user_fix(id):
    if not session.get('login'):
        return redirect('/login/')
    if session['id'] != id and not User(session['id']).admin:
        return '你没有更改该用户的权限'
    u = User(id)
    return render_template("user_fix.html", user=u, session=session)


@app.route("/user/<int:id>/fix/handle/", methods=["POST"])
def user_fix_handle(id):
    if not session.get('login'):
        return redirect('/login/')
    if session['id'] != id and not User(session['id']).admin:
        return '你没有更改该用户的权限'
    u = User(id)
    username = request.form.get("username")
    rname = request.form.get("rname")
    sign = request.form.get("sign")
    avatar = request.files.get("avatar")

    if avatar and avatar.filename != '':
        f = open("./static/user_pic/cnt.txt", 'r', encoding='utf-8')
        dat = int(f.read()) + 1
        f.close()
        f = open("./static/user_pic/cnt.txt", 'w', encoding='utf-8', newline = '\n')
        f.write(str(dat))
        f.close()
        filepath = f"{dat}{os.path.splitext(avatar.filename)[1]}"
        avatar.save(os.path.join('./static/user_pic/', filepath))
        u.picpath = filepath

    old_pwd = request.form.get("old_pwd")
    new_pwd = request.form.get("new_pwd")
    if old_pwd == u.password:
        u.password = new_pwd
    if username:
        u.username = username
    if rname:
        u.name = rname
    if sign:
        u.desc = sign
    u.save(None)
    return redirect(f"/user/{id}/")


@app.route("/user/new/")
def user_new():
    if not session.get('login'):
        return redirect('/login/')
    if session['id'] != id and not User(session['id']).admin:
        return '你没有创建新用户的权限'
    return render_template("user_new.html", session=session)


@app.route("/user/new/handle/", methods=["POST"])
def user_new_handle():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return '你没有创建新用户的权限'
    id = request.form.get("id")
    username = request.form.get("username")
    rname = request.form.get("rname")
    sign = request.form.get("sign")
    avatar = request.files.get("avatar")
    is_su = request.form.get("is_su")
    pwd = request.form.get("pwd")
    if avatar and avatar.filename != '':
        f = open("./static/user_pic/cnt.txt", 'r', encoding='utf-8')
        dat = int(f.read()) + 1
        f.close()
        f = open("./static/user_pic/cnt.txt", 'w', encoding='utf-8', newline = '\n')
        f.write(str(dat))
        f.close()
        filepath = f"{dat}{os.path.splitext(avatar.filename)[1]}"
        avatar.save(os.path.join('./static/user_pic/', filepath))
    c = get_cursor()
    cursor = c[1]
    cursor.execute("INSERT INTO users(username, password, name, level, score, active, admin, picpath, desc) VALUES(" + f"'{username}', \
        '{pwd}', '{rname}', 0, 0, 0, 0, '{filepath}', '{sign}')")
    c[0].commit()
    c[0].close()
    u = User(int(id))
    # if avatar and avatar.filename != '':
    #     u.picpath = filepath
    # u.username = username
    # u.name = rname
    # u.desc = sign
    # u.password = pws
    # u.admin = int(is_su)
    u.save(None)
    return redirect(f"/user/{id}/")


'''
团队/小组功能 部分
'''
@app.route("/group/<int:id>/")
def group(id):
    return "功能尚未上线，敬请期待！"

@app.route("/group/<int:id>/discuss/")
def group_discuss(id):
    return "功能尚未上线，敬请期待！"

@app.route("/group/<int:id>/discuss/<int:did>/")
def group_discuss_detail(id, did):
    return "功能尚未上线，敬请期待！"

@app.route("/group/<int:id>/file/")
def group_file(id):
    return "功能尚未上线，敬请期待！"


@app.route("/setting/")
def setting():
    if not session.get('login'):
        return redirect('/login/')
    if not session.get('admin'):
        return redirect('/')
    # a = session['tmp-rname']
    # b = session['tmp-eduid']
    # c = session['tmp-pwd']
    # try:
    #     d = session['tmp-id']
    # except:
    #     d = 0
    return render_template("settings.html", session=session, temp_list=get_temp_list(),
                           content_index='点击按钮以读取信息！', content_redt='点击按钮以读取信息',
                           content_main='点击按钮以读取信息', fg=forget_password_list)


@app.route("/setting/handle_res_1/", methods=['POST'])
def setting_handle_res_1():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    id = request.form.get('did', '')
    vk = request.form.get('vk', 'NO')
    if id != '':
        id = int(id)
        d = Discuss(id)
        nd = d.insert_tr(vk=vk)
        f = open(f"./discuss/{d.id}.txt", "r", encoding='utf-8')
        con = f.read()
        f.close()
        f = open(f"./resource/{nd}.txt", "w", encoding='utf-8', newline = '\n')
        f.write(con)
        f.close()
    return render_template("settings.html", session=session, temp_list=get_temp_list(),
                           content_index='点击按钮以读取信息！', content_redt='点击按钮以读取信息',
                           content_main='点击按钮以读取信息', fg=forget_password_list)


@app.route("/setting/handle_tree/", methods=['POST'])
def setting_handle_tree():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    set_search_tree()
    return render_template("settings.html", session=session, temp_list=get_temp_list(),
                           content_index='点击按钮以读取信息！', content_redt='点击按钮以读取信息',
                           content_main='点击按钮以读取信息', fg=forget_password_list)


@app.route("/setting/handle_index_1/", methods=['POST'])
def setting_handle_index_1():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    with open("./data/homework.txt", "r", encoding='utf-8') as f:
        con = f.read()
    return render_template("settings.html", session=session, content_index=con.replace('\n', '<br>'),
                           temp_list=get_temp_list(), content_redt='点击按钮以读取信息',
                           content_main='点击按钮以读取信息', fg=forget_password_list)


@app.route("/setting/handle_index_2/", methods=['POST'])
def setting_handle_index_2():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    con = request.form.get('txt', '')
    with open("./data/homework.txt", "w", encoding='utf-8', newline = '\n') as f:
        f.write(con)
    return render_template("settings.html", session=session, content_index='点击按钮以读取信息',
                           temp_list=get_temp_list(), content_redt='点击按钮以读取信息',
                           content_main='点击按钮以读取信息', fg=forget_password_list)


@app.route("/setting/handle_index_3/", methods=['POST'])
def setting_handle_index_3():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    with open("./data/tops_info.txt", "r", encoding='utf-8') as f:
        con = f.read()
    return render_template("settings.html", session=session, content_index='点击按钮以读取信息',
                           temp_list=get_temp_list(), content_redt='点击按钮以读取信息',
                           content_main=con.replace('\n', '<br>'), fg=forget_password_list)


@app.route("/setting/handle_index_4/", methods=['POST'])
def setting_handle_index_4():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    con = request.form.get('txt', '')
    with open("./data/tops_info.txt", "w", encoding='utf-8', newline = '\n') as f:
        f.write(con)
    return render_template("settings.html", session=session, content_index='点击按钮以读取信息',
                           temp_list=get_temp_list(), content_redt='点击按钮以读取信息',
                           content_main='点击按钮以读取信息', fg=forget_password_list)


@app.route("/setting/handle_activity/", methods=['POST'])
def setting_handle_activity():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    name = request.form.get('activity_name', '')
    dis = request.form.get('discuss_id', '')
    with open("./data/activity.txt", "a", encoding='utf-8', newline = '\n') as f:
        f.write('\n' + name + ':' + dis)
    return render_template("settings.html", session=session, content_index='点击按钮以读取信息',
                           temp_list=get_temp_list(), content_redt='点击按钮以读取信息', fg=forget_password_list)


@app.route("/setting/handle_activity_list/", methods=['POST'])
def setting_handle_activity_list():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    act_id = request.form.get('act_id', '')
    name = request.form.get('activity_name', '')
    dis = request.form.get('discuss_id', '')
    with open(f"./data/activity/{act_id}/.txt", "a", encoding='utf-8', newline = '\n') as f:
        f.write('\n' + name + ':' + dis)
    return render_template("settings.html", session=session, content_index='点击按钮以读取信息',
                           temp_list=get_temp_list(), content_redt='点击按钮以读取信息', fg=forget_password_list)


@app.route("/setting/handle1/", methods=['POST'])
def setting_handle1():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    name = request.form.get('docname', '')
    with open(f"./{name}.txt", "r", encoding='utf-8') as f:
        con = f.read()
    return render_template("settings.html", session=session, content=con.replace('\n', '<br>'),
                           temp_list=get_temp_list(),
                           content_redt='点击按钮以读取信息', content_index='点击按钮以读取信息',
                           fg=forget_password_list)


@app.route("/setting/handle2/", methods=['POST'])
def setting_handle2():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    name = request.form.get('docname', '')
    con = request.form.get('txt', '')
    with open(f"./{name}.txt", "w", encoding='utf-8', newline = '\n') as f:
        f.write(con)
    return render_template("settings.html", session=session, content='', content_redt='点击按钮以读取信息',
                           temp_list=get_temp_list(),
                           content_index='点击按钮以读取信息', fg=forget_password_list)


@app.route("/setting/handle_redt_1/", methods=['POST'])
def setting_handle_redt_1():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    with open("./data/redt.txt", "r", encoding='utf-8') as f:
        con = f.read()
    return render_template("settings.html", session=session, content_index='点击按钮以读取信息',
                           content_redt=con.replace('\n', '<br>'), temp_list=get_temp_list(), fg=forget_password_list)


@app.route("/setting/handle_redt_2/", methods=['POST'])
def setting_handle_redt_2():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    con = request.form.get('txt', '')
    with open("./data/redt.txt", "w", encoding='utf-8', newline = '\n') as f:
        f.write(con)
    return render_template("settings.html", session=session, content_index='点击按钮以读取信息',
                           content_redt='点击按钮以读取信息', temp_list=get_temp_list(), fg=forget_password_list)


@app.route("/setting/handle_learn/", methods=['POST'])
def setting_handle_learn():
    if not session.get('login'):
        return redirect('/login/')
    if not User(session['id']).admin:
        return redirect('/')
    subject = request.form.get('subject')
    year = request.form.get('year')
    idx = request.form.get('idx')
    discuss_id = request.form.get('discuss_id')
    with open("./data/learn.txt", "r+", encoding='utf-8', newline = '\n') as f:
        learn = f.read().split('>\n')
        learn[int(subject) + 1] = learn[int(subject) + 1] + year + '_' + idx + ':' + discuss_id + '\n'
        con = '>\n'.join(learn)
        f.seek(0)
        f.write(con)
    return render_template("settings.html", session=session, content_index='点击按钮以读取信息',
                           content_redt='点击按钮以读取信息', temp_list=get_temp_list(), fg=forget_password_list)


@app.route("/setting/handle_fgpwd/", methods=['GET', 'POST'])
def setting_handle3():
    id = request.form.get("id")
    pwd = request.form.get("pwd")
    u = User(id=int(id))
    u.password = pwd
    u.save(None)
    return render_template("sucess.html", session=session)


@app.route('/about/')
def about():
    return render_template('about.html', session=session)


@app.route('/about/<string:path>/')
def about_shell(path):
    f = open(f"./info/about/{path}.txt", 'r', encoding='utf-8')
    con = f.read()
    f.close()
    return render_template('about_shell.html', session=session, content=con)


'''
@app.route("/error500/")
def error500page():
    return render_template("500.html", session=session)


@app.route("/error404/")
def error404page():
    return render_template("404.html", session=session)
'''


@app.errorhandler(404)
def error404(error):
    return render_template("404.html", session=session), 404


@app.errorhandler(500)
def error500(error):
    return render_template("500.html", session=session), 500

@app.errorhandler(502)
def error502(error):
    return "There is an exception : 502 BAD GATEWAY.（网关爆炸，可能因为服务器离线了，请联系开发人员）", 502


if __name__ == "__main__":
    if debugrun:
        print("Serving Flask app 'main'")
        print("DEBUG MODE : ON")
        print("RUNNING ON 0.0.0.0 PORT 8000")
        print('This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.')
        logging.warning('This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.')
        app.run(host='0.0.0.0', port=8000, debug=True)
    else:
        print("Serving Flask app 'main'")
        print("DEBUG MODE : OFF")
        print("RUNNING ON 0.0.0.0 PORT 8000")
        logging.info("Serving Flask app 'main'")
        logging.debug("DEBUG MODE : OFF")
        logging.info("RUNNING ON 0.0.0.0 PORT 8000")
        httpd = make_server('0.0.0.0', 8000, app)
        httpd.serve_forever()
