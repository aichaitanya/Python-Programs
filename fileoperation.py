# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:24:02 2019

@author: Patil
"""


def write(name,path):
    file=str(path)+'\\'+str(name)
    f=open(str(file),'w')
    print('Enter Content + @ at the end : ')
    s=''
    while(s!='@'):
        s=input()
        if s!='@':
            f.write(s)
    print('File Successful')
    f.close()

def read(name,path):
    file=str(path)+'\\'+str(name)
    f=open(str(file),'r')
    print(f.read())
    f.close()

def append(name,path):
    file=str(path)+'\\'+str(name)
    f=open(str(file),'a+')
    print('Enter Content @ : ')
    s=''
    while(s!='@'):
        s=input()
        if s!='@':
            f.write(s)
    print('Write Successful')
    print(f.read())
    f.close()


ch=1

name=input('File Name with ext : ')
path = input('Enter Directory : ')

while ch==1:
    print('1.Write 2.Read 3. Append')
    op=int(input('Enter Option : '))
    if op==1 :
        write(name,path)
    elif op==2 :
        read(name,path)
    elif op==3 :
        append(name,path)
    else : print('Invalid')
    ch=int(input('Continue 1/0 :'))


'''
File Name with ext : hello5.txt

Enter Directory : C:\Chaitanya\Python
1.Write 2.Read 3. Append

Enter Option : 1
Enter Content + @ at the end : 

Hello World 

@
File Successful

Continue 1/0 :1
1.Write 2.Read 3. Append

Enter Option : 2
Hello World 

Continue 1/0 :1
1.Write 2.Read 3. Append

Enter Option : 3
Enter Content @ : 

Hello There

@
Write Successful


Continue 1/0 :1
1.Write 2.Read 3. Append

Enter Option : 2
Hello World Hello There

Continue 1/0 :0

'''