# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:05:08 2021

@author: 20b-049-cs
"""
from Array import Array

myarray = Array(10)
print('The length of array is:',len(myarray))
for i in range(len(myarray)):
    item = random.random()
    print('{} --> {:.2f}'.format(i,item))
    myarray[i] = item
    
print('Array initialized up to {}'.format(len(myarray)))
aindex = int(input("Enter the index value of array element: "))

print('The array index {} contains item {:.2f}'.format(aindex,myarray[aindex]))