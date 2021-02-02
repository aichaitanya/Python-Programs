# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:02:17 2019

@author: Patil
"""

n = int(input('Enter Range : '))

print('Fibonacci Series\n')
a=0
b=1

if n==1: 
    print('0')
elif n==2: 
    print('0\n1')
else : 
    print('0\n1')
    for i in range(2,n):
        c=a+b
        print(c)
        a=b
        b=c

'''
Enter Range : 7
Fibonacci Series

0
1
1
2
3
5
8

'''