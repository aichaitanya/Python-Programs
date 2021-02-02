# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:27:05 2019

@author: Patil
"""
import array as t
arr=t.array('i',[])

n=int(input('Enter Size : '))
for i in range(n):
    b=int(input('Enter Element : '))
    arr.append(b)

print('UnSorted ....')
print(arr)

def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 
		L = arr[:mid]
		R = arr[mid:]
		mergeSort(L)
		mergeSort(R)

		i = j = k = 0
		
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+=1
			else: 
				arr[k] = R[j] 
				j+=1
			k+=1
		
		while i < len(L): 
			arr[k] = L[i] 
			i+=1
			k+=1
		
		while j < len(R): 
			arr[k] = R[j]
			j+=1
			k+=1
            
mergeSort(arr)
print('Sorted ....')
print(arr)

'''
Enter Size : 5

Enter Element : 33

Enter Element : 45

Enter Element : 67

Enter Element : 52

Enter Element : 31
UnSorted ....
array('i', [33, 45, 67, 52, 31])
Sorted ....
array('i', [31, 33, 45, 52, 67])

'''