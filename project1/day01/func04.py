# -*- coding: utf-8 -*-
'''
  加入购物车
  判断用户的登录地址

'''


def func(number):
    a = 100
    
    
    def inner_func():
        nonlocal a
        nonlocal number
        for i in range(number):
            a +=1
        
        
        print('修改后的的a:', a)
    return inner_func


#调用
f = func(5)
f()


a = 50

f1 = func(a)
print(f1)


#地址引用
def test():
    print('-----test-----')

t = test
    
def decorate(func):
    a =100
    print('wrapper外层打印测试')
    def wrapper():
        func()
        print('------>刷地板')
        print('------>装门窗')
        print('------>精装房')
    print('wrapper加载完成.....')
    return wrapper
@decorate
def house():
    print('我是毛坯房')
    
house()
    