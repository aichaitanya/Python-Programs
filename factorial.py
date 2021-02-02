# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:45:44 2019

@author: Patil
"""
n=int(input('Enter Number : '))

def fact(n):
    if n==1:
        return 1
    else :
        return n*fact(n-1)

print("Factorial is %d" % fact(n))