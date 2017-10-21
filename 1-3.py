#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
@Author:jackpler
'''

str = raw_input('输入字符串：')

vowels = ['a','i','o','u','e']

count = {}

for s in str:
    if s in vowels:
        count[s] = count.get(s,0) + 1

for k,v in count.items():
    print('%s出现了%d次'%(k,v))
