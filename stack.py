# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:00:19 2019

@author: Patil
"""

a = []

def printstk():
    for i in a:
        print(i)
    
def push(a):
    ele=int(input('Enter element : '))
    a.append(ele)

def pop(a):
    if(top!=-1):
        print(a.pop(),'Popped')
    else : print('Stack Underflow')
    
ch=1
top=-1
while(ch==1):
    print('1. Push 2. Pop 3. Print')
    op=int(input('Enter Option : '))
    if op==1:
        push(a)
        top+=1
    elif op==2:
        pop(a)
        top-=1
    elif op==3:
        printstk()
    else : print('Invalid')
    
    print('Current Stack : ')
    if top!=-1:
        printstk()
    else : print('Underflow')
    ch=int(input('Continue 1/0 : '))
    
    
'''
1. Push 2. Pop 3. Print

Enter Option : 1

Enter element : 11
Current Stack : 
11

Continue 1/0 : 1
1. Push 2. Pop 3. Print

Enter Option : 1

Enter element : 22
Current Stack : 
11
22

Continue 1/0 : 1
1. Push 2. Pop 3. Print

Enter Option : 1

Enter element : 33
Current Stack : 
11
22
33

Continue 1/0 : 1
1. Push 2. Pop 3. Print

Enter Option : 1

Enter element : 44
Current Stack : 
11
22
33
44

Continue 1/0 : 1
1. Push 2. Pop 3. Print

Enter Option : 1

Enter element : 55
Current Stack : 
11
22
33
44
55

Continue 1/0 : 1
1. Push 2. Pop 3. Print

Enter Option : 2
55 Popped
Current Stack : 
11
22
33
44

Continue 1/0 : 1
1. Push 2. Pop 3. Print

Enter Option : 2
44 Popped
Current Stack : 
11
22
33

Continue 1/0 : 1
1. Push 2. Pop 3. Print

Enter Option : 3
11
22
33
Current Stack : 
11
22
33

Continue 1/0 : 1
1. Push 2. Pop 3. Print

Enter Option : 3
11
22
33
Current Stack : 
11
22
33

Continue 1/0 : 1
1. Push 2. Pop 3. Print

Enter Option : 2
33 Popped
Current Stack : 
11
22

Continue 1/0 : 1
1. Push 2. Pop 3. Print

Enter Option : 2
22 Popped
Current Stack : 
11

Continue 1/0 : 1
1. Push 2. Pop 3. Print

Enter Option : 2
11 Popped
Current Stack : 
Underflow

'''
    