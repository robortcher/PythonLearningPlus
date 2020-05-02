# -*- coding: utf-8 -*-
'''
    用户登录
    输入用户名
    输入密码
    输入验证码
'''


import random

#定义函数
def generate_checkcode(n):
     s = 'asfab12jb42j14b9309ENKEWEWWQQWQEQWRQR'
     code =''
     for i in range(n):
         ran = random.randint(0, len(s)-1)
         code += s[ran]
     return code

def login():
    username = input('输入用户名： ')
    password = input('输入密码: ')
    #得到一个验证码
    code = generate_checkcode(5)
    print('验证码是：', code)
    code1 = input('请输入验证码：')
    #验证
    if code.lower() == code1.lower():
        #验证码输入正确
        if username =='lijiaqi' and password == '123456':
            print('用户登陆成功')
        else:
            print('用户名或密码输入有误')
    else:
        print('验证码输入有误')

login()



