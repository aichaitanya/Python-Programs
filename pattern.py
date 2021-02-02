# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 20:40:42 2019

@author: Patil
"""

n = int(input('Enter Lines : '))

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()
    
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for j in range(i,0,-1):
        print('*',end="")
    for j in range(2,i+1):
        print('*',end="")
    print()
    

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end="")
    print()
    
print()

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for j in range(1,i+1):
        print(j,end="")
    print()

print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

print()

for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
    
for i in range(1,n+1):
    print('*'*i)
    
print()

for i in range(n,0,-1):
    print('*'*i)

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()
for i in range(1,n):
    for j in range(i):
        print(end=" ")
    for j in range(n-i,0,-1):
        print(j,end="")
    for i in range(2,n-1):
        for j in range(2,n):
            print(j,end="")
        
    print()
    

    '''
Enter Lines : 4
   1
  212
 32123
4321234
   *
  ***
 *****
*******
   1
  21
 321
4321

   1
  12
 123
1234

1
12
123
1234

1
21
321
4321
*
**
***
****

****
***
**
*
//Try This IF You Can Diamond Shape
   1
  212
 32123
4321234
 32123
  2123
   123

    '''