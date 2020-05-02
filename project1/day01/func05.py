# -*- coding: utf-8 -*-
import time 

user_df = {'xiao':{'password':'19940929', 'balance':100000}}

islogin = False

def login():
    print('=======欢迎进入支付页面====')
    global user_df
    global islogin
    islogin = False
    username = input('请输入用户名(q为退出支付)：')
    password = input('请输入密码：')
    if username in user_df and user_df[username]['password'] == password:
        islogin = True
    elif username =='q':
        print('退出支付')
    else:
        print('账号密码输入有误，请重新输入')
        login()


def login_required(func):
    def wrapper(*args, **kwargs):
        #验证用户是否登录
        global islogin
        while not islogin:
            print('用户没有登陆，无法付款')
            print('正在跳转登陆页面......')
            time.sleep(2)
            login()
        else:
            print('账号登陆成功，本次支付金额{}元'.format(*args))
            func(*args, **kwargs)
    return wrapper

@login_required
def pay(money):
    print('正在付款，付款金额: {}元'.format(money))
    print('付款中......')
    
    time.sleep(2)
    print('付款完成')



