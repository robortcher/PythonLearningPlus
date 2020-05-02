# -*- coding: utf-8 -*-
'''
conditions:
    1.外部函数定义了内部函数
    2.外部函数有返回值
    3.返回值：内部函数名
    4.引用外部函数变量值
    
functions:
    1.保存返回闭包时的状态
    2.装饰器
'''



def func(a, b):
    c = 10
    
    
    def inner_func():
        s = a+b+c
        print('相加之后的结果是：',s)
    
    return inner_func





