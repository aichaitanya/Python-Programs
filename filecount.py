# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:44:28 2019

@author: Patil
"""

file=input('Enter Path Of File With EXT : ')

line=0
words=0
chars=0

with open(file,'r') as f:
    for x in f:
        word=x.split()
        line+=1
        words+=len(word)
        chars+=len(x)
        
print('Lines : ',line)
print('Words : ',words)
print('Chars : ',chars)

'''

hello how are 
you

Enter Path Of File With EXT : C:\Chaitanya\Python\hello.txt
Lines :  2
Words :  4
Chars :  18
'''