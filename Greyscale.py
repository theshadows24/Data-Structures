# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:59:04 2021

@author: 20b-049-cs
"""

from Array2D import Array2D

class GrayscaleImage:
    def __init__(self, nrows, ncols):
        self._image = Array(nrows)
        for i in range(nrows):
            self._image[i] = Array(ncols)
        self._image.clear(0)
        
    def width(self):
        return len(self._image)
    
    def height(self):
        return len