# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 11:33:07 2020

@author: Patil
"""

class pattern:
    def star():
        n = int(input('Enter : '))
        s=(n*2)-2
        for i in range(1,n+1):
            for sp in range(s): #Space
                print(" ",end="")
            s-=2

            for j in range(i):
                print((i+1)%2,'  ',end="")
            print()
class  patter():    
    def aPatt():
        n = int(input('Enter : '))
        s=(n*2)-2
        for i in range(1,n+1):
            for sp in range(s): #Space
                print(" ",end="")
            s-=2

            for j in range(i):
                print(chr(64+i),'  ',end="")
            print()
class patte():    
    def ABCD():
        n = int(input('Enter : '))
        s=(n*2)-2
        c=64
        for i in range(1,n+1):

            for sp in range(s): #Space
                print(" ",end="")
            s-=2
            for j in range(1,i+1):
                print(chr(c+j),'  ',end="")
            c+=j
            print()
