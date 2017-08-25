#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#逆转字符串

temp = raw_input('输入字符串：')

#1.切片方式
print(temp[::-1])

#2.List方式
s = list(temp)
s.reverse()
print(''.join(s))

#3.reduce方式
from functools import reduce
print(reduce(lambda x,y : y+x,temp))
