from password import password
import base
import ip
import pyperclip
import time
import threading
import requests
from tkinter import *
print('RCL聊天工具')
try:
    a=input('请设置名字')
    v=input('请设置密码')
    if v=='':
        v='N'
    ipc=ip.d
    g=password(a,v,ipc)
    h=str(g)
    # copies all the data the user has copiedg
    pyperclip.copy(h)
    pyperclip.paste()
    print('聊天码已经复制到剪切板了，按chrl+v粘贴')
    print('如果没有，可以复制聊天码:',h)
    time.sleep(2)
    time.sleep(2)
    s = input('请输入对方发来的聊天码')
    s = s.split('.')
    w = s[0]
    f = s[1]
    d = s[2]
    v = base.base(2, w)
    c = base.base(2, f)
    b = base.base(2, d)
    userid = v
    password = c
    ipc = b
    start = time.perf_counter()
except:
    print('程序遇到问题，请退出重试或报给bug')
def server():
    global userid,password,ipc
    url = 'http://{0}:8080'.format(ipc)
    import urllib.request  # 引入urllib.request
    import ssl
    # This restores the same behavior as before.
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url)  # 打开URL
    html = response.read()  # 读取内容
    html = html.decode('GBK')  # 解码
    a = html[34:]
    p = a.split()
    old = p[0]
    time.sleep(0.01)
    if old != p[0]:
        print(userid + p[0])
def answer():
    global a,userid
    try:
        url = 'http://{0}:8080'.format(ipc)
        r = requests.get(url, timeout=5)
        code = r.status_code
        if code == 200:
            print('已连接成功')
            print('{0}和{1}的聊天室'.format(userid,a))
            t = 0
            a = input('请输入内容')
            while True:
                if t == 1:
                    a = input()
                # 编辑html文件

                f = open('index.html', 'w')
                message = """<html>
                <head></head>
                <body>
                <p>
                """ + a + """
                </p></body>
                </html>"""
                f.write(message)
                f.close()
                print('袁梓宸:' + a)
                t = 1
        else:
            print('连接失败，请稍后再试')
    except:
        print('程序遇到问题，请退出重试或报给bug')
thread1 = threading.Thread(target=server)
thread2 = threading.Thread(target=answer)

thread1.start()
thread2.start()

finish = time.perf_counter()
