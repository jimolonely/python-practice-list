#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def is_palindrome(low,high,s):
    len = high - low + 1
    if len==0 or len==1:#考虑字符长度为奇数或偶数
        return True
    if s[low] != s[high]:
        return False
    return is_palindrome(low+1,high-1,s)

s = raw_input('输入字符串：')
len = len(s)

print('%s是回文：'%s)
print(is_palindrome(0,len-1,s))
