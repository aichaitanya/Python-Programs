# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 20:15:38 2019

@author: Patil
"""

a = int(input('Enter Number 1 : '))
b = int(input('Enter Number 2 : '))

ch=1
while(ch==1):
    print('1. Add 2. Sub 3. Mul 4. Div 5. Mod 6. Exp\n ')
    o = input('Enter Option : ')
    if o=='+':
        print('Add : ',a+b)
    elif o=='-': 
        print('Sub : ',a-b)
    elif o=='*' :
        print('Mul : '.a*b)
    elif o=='/':
        print('Div : ',a/b)
    elif o=='%':
        print('Mod : ',a%b)
    elif o=='**':
        print('Exp : ',a**b)
    else : print('Wrong Option')
    print('Want to continue (0 N / 1 Y) :')
    ch=int(input())

'''
Enter Number 1 : 2

Enter Number 2 : 3
1. Add 2. Sub 3. Mul 4. Div 5. Mod 6. Exp
 

Enter Option : **
Exp :  8
Want to continue (0 N / 1 Y) :

1
1. Add 2. Sub 3. Mul 4. Div 5. Mod 6. Exp
 

Enter Option : %
Mod :  2
Want to continue (0 N / 1 Y) :

0

'''

