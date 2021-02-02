# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:48:50 2019

@author: Patil
"""
import array as arr

ar=arr.array('i',[])

n = int(input('Enter size : '))

for i in range(n):
    a=int(input('Enter Elements : '))
    ar.append(a)
    
def sort(ar,n):
    for i in range(1,n):
        for j in range(n-i):
            if ar[j]>ar[j+1] :
                temp=ar[j]
                ar[j]=ar[j+1]
                ar[j+1]=temp      
    print(ar)

def binsearch(ar,n):
    sort(ar,n)
    key=int(input('Enter Key : '))
    pos=-1
    l=0
    h=n-1
    while(l<=h):
        mid=int((l+h)/2)
        if ar[mid]==key:
            pos=mid
            break
        elif ar[mid]>key:
            h=mid-1
        else : l=mid+1
    if pos!=-1:
        print('Key Found : ',pos)
    else : print('Not Found')

ch=1
while(ch==1):   
    binsearch(ar,n)
    ch=int(input('Continue 1/0 : '))
    
    '''
    Enter size : 5

Enter Elements : 76

Enter Elements : 54

Enter Elements : 32

Enter Elements : 45

Enter Elements : 78
array('i', [32, 45, 54, 76, 78])

Enter Key : 76
Key Found :  3

Continue 1/0 : 1
array('i', [32, 45, 54, 76, 78])

Enter Key : 78
Key Found :  4

Continue 1/0 : 1
array('i', [32, 45, 54, 76, 78])

Enter Key : 32
Key Found :  0

Continue 1/0 : 1
array('i', [32, 45, 54, 76, 78])

Enter Key : 45
Key Found :  1

Continue 1/0 : 1
array('i', [32, 45, 54, 76, 78])

Enter Key : 54
Key Found :  2

Continue 1/0 : 0
    
    '''
    