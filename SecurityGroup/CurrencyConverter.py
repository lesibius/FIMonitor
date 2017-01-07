# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 17:23:57 2017

@author: clem
"""

class CurrencyConverter:
    """
    Class responsible for the conversion of currencies
    """
    def __init__(self):
        self.Currencies = set()
        self.ConversionTable = {}
        
    def AddCurrency(self,iso):
        if not iso in self.Currencies:
            self.Currencies.add(iso)
            if len(self.Currencies) > 0:
                for c in self.Currencies:
                    self.ConversionTable[(iso,c)]=1
                    self.ConversionTable[(c,iso)]=1
    
    def SetExchangeRate(self,iso1,iso2,rate):
        if iso1 in self.Currencies and iso1 in self.Currencies:
            self.ConversionTable[(iso1,iso2)]=rate
            self.ConversionTable[(iso2,iso1)]=1/rate
        else:
            raise Exception