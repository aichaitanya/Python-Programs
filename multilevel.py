# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:01:38 2019

@author: Patil
"""

class student:
    def __init__(self,fname):
        self.name=fname
    def show(self):
        print("Name : ",self.name)
        
class marks(student):
    def __init__(self,m1,m2,fname):
        self.sem1=int(m1)
        self.sem2=int(m2)
        self.total=0
        student.__init__(self,fname)
    def detail(self):
        self.show()
        self.total=self.sem1+self.sem2
        print("Total : ",self.total)
    
class output(marks):
    def __init__(self,fname,m1,m2,year):
        self.yr=year
        marks.__init__(self,m1,m2,fname)
    def result(self):
        self.detail()
        print("Year : ",self.yr)
        
    
a=input('Enter Name : ')
b=(input('Enter Marks 1 : '))
c=input('Enter Marks 2 : ')
d=input('Enter Year : ')

obj=output(a,b,c,d)
obj.result()

'''
Enter Name : Chaitanya

Enter Marks 1 : 700

Enter Marks 2 : 800

Enter Year : May 2018
Name :  Chaitanya
Total :  1500
Year :  May 2018

'''
        