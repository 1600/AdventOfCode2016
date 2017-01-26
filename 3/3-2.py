#!coding=utf-8
import numpy as np
import os
import re
input_dic = []
triangle_num = 0

def isTriangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

with open('input.txt','r') as f:
    temp = []
    for i in f.readlines():
        a =i.split()
        c = map(int,a)
        temp.append(c)

    for i in xrange(3):
        a = [row[i] for row in temp]
        for i in xrange(0,len(a),3):
            print a[i],a[i+1],a[i+2]
            if isTriangle(a[i],a[i+1],a[i+2]):
                triangle_num+=1
                
print triangle_num

