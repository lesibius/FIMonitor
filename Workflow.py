# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 18:41:22 2017

@author: clem
"""

from sets import Set

class Workflow:
    
    def __init__(self):
        self.Portfolios = []
        self.EconomicModels = []
        
    def SetNewPortfolio(self):
        self.Portfolios