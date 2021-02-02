# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:51:31 2019

@author: Patil
"""

a = input('Enter String : ')
aa=a.lower()
b=a
c=b[::-1]
cc=c.lower()

if cc==aa:
    print('palindrome')
else : print('not')

'''
Enter String : romororomor
palindrome

Enter String : Madam
palindrome

Enter String : tesla
not

'''