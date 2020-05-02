# -*- coding: utf-8 -*-
import time
def decorate(func):
    def wrapper(*x):
        print('正在校验中...')
        time.sleep(2)
        print('校验完毕...')
        func(*x)
    return wrapper


@decorate

def f1(n1, n2):
    print('----f1----', n1, n2)

@decorate
def f2(name):
    print('----f2----', name)

@decorate
def f3(li):
    for i in li:
        print('----f3----', i)



f1(1, 3)
f2('Xiao')
f3([1,2, 3])
         

 