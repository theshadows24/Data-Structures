# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 22:31:26 2021

@author: Ifra
"""
from Array2D import Array2D

class Matrix:
    def __init__(self, numRows, numCols):
        self._theGrid = Array2D(numRows,numCols)
        self.determinant = 0
        self._theGrid.clear(0)
        
    def numRows(self):
        return self._theGrid.numRows()
    
    def numCols(self):
        return self._theGrid.numCols()
    
    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0],ndxTuple[1]]
    
    def __setitem__(self, ndxTuple, scalar):
        self._theGrid[ndxTuple[0],ndxTuple[1]] = scalar
        
    def scaleBy(self, scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r,c] *= scalar
        
    def transpose(self):
        newMatrix = Matrix(self.numRows(),self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r,c] = self[c,r]
        return newMatrix
                
    def __add__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols() == self.numCols(), "Matrices' sizes not compatible for addition"
        newMatrix = Matrix(self.numRows(),self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r,c] = self[r,c] + rhsMatrix[r,c]
        return newMatrix
    
    def __sub__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numRows() and rhsMatrix.numCols() == self.numCols(), "Matrices' sizes not compatible for addition"
        newMatrix = Matrix(self.numRows(),self.numCols())
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                newMatrix[r,c] = self[r,c] - rhsMatrix[r,c]
        return newMatrix
        
    def __mul__(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numCols(), "Matrices' sizes not compatible for addition"
        newMatrix = Matrix(self.numRows(),self.numCols())
        #at the row of selfMatrix
        for r in range(self.numRows()):
            #at the column of otherMatrix
            for c in range(rhsMatrix.numCols()):
                #at the row of otherMatrix
                for k in range(rhsMatrix.numRows()):
                    newMatrix[r,c] += self[r,k]*rhsMatrix[k,c]
        return newMatrix
    
    def matrixMinor(self,i,j):
        assert self.numRows() == self.numCols(), "Matrix should be square"
#        i = 0
#        j = self.numRows()
        self.minor = Array2D(self.numRows()-1,self.numCols()-1)
        for row in range(self[0,i] + self[i+1,0]):
            self.minor[i,j] = row[0,j] + row[j+1,0]
            #very much slicing ka masla
        
    def matrixBaseDet(self):
        assert self.numRows() == self.numCols(), "Matrix should be square"
        self.baseDet = self[0,0]*self[1,1] - self[0,1]*self[1,0]
        return self.baseDet
        
    def matrixDet(self):
        assert self.numRows() == self.numCols(), "Matrix should be square"
        self.determinant = 0
        for c in range(self.numRows()):
            minor = self.matrixMinor(0,c)
            self.determinant += ((-1)**c)*self[0,c]*minor.matrixBaseDet()
        return self.determinant
    
    def matrixInverse(self):
        assert self.numRows() == self.numCols(), "Matrix should be square"
        assert self.determinant != 0, "Determinant is 0"
        if self.numRows() == 2:
            det = self.matrixBaseDet()
            inverse = [[self[1,1]/self.determinant, -1*self[0,1]/self.determinant],
                       [-1*self[1,0]/self.determinant, self[0,0]/self.determinant]]
        else:
            det = self.matrixDet()
            cofactors = Array2D(self.numRows,self.numCols)
            for r in range(self.numRows()):
                cofactorRow = Array(self.numRows)
                for c in range(self.numRows()):
                    minor = self.matrixMinor(self,r,c)
                    cofactorRow.append(((-1)**(r+c))*minor.matrixDet())
                cofactors.append(cofactorRow)
            cofactors = transposeMatrix(cofactors)
            for r in range(len(cofactors)):
                for c in range(len(cofactors)):
                    cofactors[r,c] = cofactors[r,c]/determinant
            return cofactors
            