# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:27:42 2021

@author: 20b-049-cs
"""
from Matrix import Matrix

def matrix_enter(A):
    for i in range(A.numRows()):
        print('')
        for j in range(A.numCols()):
            A[i,j] = int(input(f'Enter value at ({i},{j}) '))
    return A

def matrix_format(A):        
    print('The created matrix :')
    for i in range(A.numRows()):
        print('|', end='')
        for j in range(A.numCols()):
            print(A[i,j],end=" ")
        print('|\n',end='')
        
        
A = Matrix(2,2)   
matrix_enter(A)    
matrix_format(A) 
#B = Matrix(2,2)
#matrix_enter(B)
#matrix_format(B)

C = A*B
matrix_format(C)
A.matrixDet()
matrix_format(A)
