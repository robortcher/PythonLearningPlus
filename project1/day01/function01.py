# -*- coding: utf-8 -*-

import random


def generate_random(number):
    for i in range(number):
        ran = random.randint(1, 10)
        print(ran)
    

print(generate_random)


#调用
a = generate_random(5)

b = generate_random(8)

def add(args):
    if isinstance(args[-1], str):
        sum_  = 0 
        if len(args) > 1:
            for i in args[:-1]:
                sum_ += i
            print('{}累加和为{}'.format(args[-1], sum_))
        else:
            print('{}没有元素可以向求和'.format(args[-1]))
    else:
        sum_  = 0
        if len(args) > 0:
           for i in args:
               sum_ += i
               print('累加和为{}'.format(sum_))
        else:
            print('没有元素可以向求和')
add((1, 2, 3, '肖明晖'))