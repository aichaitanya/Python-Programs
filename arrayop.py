# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 11:04:45 2019

@author: Patil
"""

import array as t

a=t.array('i',[])
n=int(input('Enter Size : '))

for i in range(n):
    b=int(input('Enter Elements : '))
    a.append(b)

def count():
    ct=int(input('Enter Number to be count : '))
    print(a.count(ct))

def length():
    print(len(a))

def index():
    i=int(input('Enter Element : '))
    print(a.index(i))
    
def insert():
    loc=int(input('Enter Loc : '))
    ele = int(input('Enter Element : '))
    a.insert(loc,ele)
    print(a)
    
def pop():
    p=int(input('Enter Location To be Popped : '))
    a.pop(p)
    print(a)    
    
def remove():
    de=int(input('Enter Element to be removed : '))
    a.remove(de)
    print(a)
    
def insert():
   inp=int(input('Enter Element to be inserted : '))
   loc=int(input('Enter Loc : '))
   a.insert(loc,inp)
   print(a)
   
count()
length()
index()
pop()
remove()
insert()

'''
Enter Size : 5

Enter Elements : 5

Enter Elements : 4

Enter Elements : 3

Enter Elements : 2

Enter Elements : 1

Enter Number to be count : 4
1
5

Enter Element : 3
2

Enter Location To be Popped : 2
array('i', [5, 4, 2, 1])

Enter Element to be removed : 2
array('i', [5, 4, 1])

Enter Element to be inserted : 3

Enter Loc : 2
array('i', [5, 4, 3, 1])

'''