# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:21:39 2019

@author: Patil
"""

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
        
class marks:
    def __init__(self,m1,m2):
        self.sem1=int(m1)
        self.sem2=int(m2)
        self.total=0
    def detail(self):
        self.total=self.sem1+self.sem2
        print("Total : ",self.total)
    
class output(student,marks):
    def __init__(self,fname,m1,m2,year):
        self.yr=year
        student.__init__(self,fname)
        marks.__init__(self,m1,m2)
    def result(self):
        self.show()
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
        