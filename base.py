def base(x, y):
    import base64
    if x == 1:
        encodestr = base64.b64encode(y.encode('utf-8'))
        return str(encodestr, 'utf-8')
    if x == 2:
        encodestrn = base64.b64decode(y.encode('utf-8'))
        return str(encodestrn, 'utf-8')
def answer(state):
        import sys, time
        import os  # 导入os模块  # 导入sys模块
        f_handler = open('practice.log', 'w')  # 使用open函数，选择仅写入文件的格式'w'，打开一个文件，此时的文件名为practice.log
        oldstdout = sys.stdout  # sys.stdout是Python默认的标准输出，先将它保存到一个变量oldstdout当中
        sys.stdout = f_handler  # 将Python标准输出指向practice.log文件
        os.system('cls')  # 清空Python控制台
        sys.stdout = oldstdout
        if state==1:
            print('base64加密程序')
        try:
            while True:
                if state==1:
                    a = input('加密输入1,解密输入2,返回输入3')
                elif state==2:
                    a = input('加密输入1,解密输入2,退出输入3')
                if int(a) == 1:
                    d = input('请输入要加密的字符:')
                    f = base(1, str(d))
                    print('加密结果为:{0}'.format(f))
                if int(a) == 2:
                    d = input('请输入要解密的字符:')
                    g = base(2, str(d))
                    print('解密结果为:{0}'.format(g))
                if int(a) == 3:
                    if state==0:
                        break
                        import sys
                        sys.exit()
                    elif state==1:
                        from main_new import start
                        start()
        except:
            print('输入的字符无效')
if __name__ == "__main__":
    answer(0)