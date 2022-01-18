# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:13:38 2021

@author: 20b-049-cs
"""
from Array2D import Array2D

twoDArray = Array2D(3,3)
twoDArray.clear(0)

for i in range(twoDArray.numRows()):
    print('')
    for j in range(twoDArray.numCols()):
        twoDArray[i,j] = int(input(f'Enter value at ({i},{j}) '))
        
print('Your 2d Array is here:')
for i in range(twoDArray.numRows()):
    print('')
    for j in range(twoDArray.numCols()):
        print(twoDArray[i,j],end=" ")