# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 15:55:40 2017

@author: clem
"""

class Loss:
    
    def __init__(self,relative,mv):
        self.BasisMarketValue = mv
        self.Relative = relative
        self.Absolute = mv * relative
        
    def __add__(self,other):
        totalMV = self.BasisMarketValue + other.BasisMarketValue
        tempRelative = (self.Absolute + other.Absolute)/totalMV
        return Loss(tempRelative,totalMV)