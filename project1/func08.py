# -*- coding: utf-8 -*-
def outer(a): #带参数的装饰器
    def decorate(func):
        def wrapper(*args, **kwargs):
            func(*args)
            print('----->铺地砖{}块'.format(a))
        return wrapper
    return decorate


@outer(a=10)
def house(date):
    print('我{}拿到房子的钥匙， 是毛坯房...'.format(date))
    
house('2020-02-31')


@outer(200)
def street(name):
    print('新修{}街道'.format(name))

street('河北大道')