# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 20:30:18 2019

@author: Patil
"""

num = int(input("Please Enter any num: ")) 
n=num  
Reverse = 0    
while(num > 0):    
    Reminder = num %10    
    Reverse = (Reverse *10) + Reminder    
    num = num //10
print("\nReverse of entered num is = ",Reverse)  

sum = 0
while(n > 0):
    dig=n%10
    sum+=dig
    n=n//10
print("The sum is",sum)


'''
Please Enter any num: 1234

Reverse of entered num is =  4321
The sum is 10 '''