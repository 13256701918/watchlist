# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:51:59 2020

@author: jiuyang.wei
"""
import random
import string
#数字+字母+符号
def getRandChar(n):
    l = []  
    #sample = '0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()-+=.'
    sample = random.sample(string.ascii_letters + string.digits, 62)## 从a-zA-Z0-9生成指定数量的随机字符： list类型
    for i in range(n):
        char = random.choice(sample)#从sample中选择一个字符
        l.append(char)
    return ''.join(l)#返回字符串
a=getRandChar(32)
b=list(a)
b.sort()
a="".join(b)
print(a)