#!coding=utf-8
import os
input_dic = []
triangle_num = 0

def isTriangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

with open('input.txt','r') as f:
    for i in f.readlines():
        a =i.split()
        c = map(int,a)
        print c
        if isTriangle(c[0],c[1],c[2]):
            triangle_num+=1

print triangle_num

