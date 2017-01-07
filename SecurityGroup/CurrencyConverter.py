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
        """
        Add a currency to the CurrencyConverter instance
        
        Parameters
        ----------
        iso: str
            ISO code of the currency
            
        Returns:
        --------
        None
        """
        if not iso in self.Currencies:
            self.Currencies.add(iso)
            if self.Currencies:
                for c in self.Currencies:
                    self.ConversionTable[(iso,c)]=1
                    self.ConversionTable[(c,iso)]=1
    
    def SetExchangeRate(self,base,quotation,rate):
        """
        Set the exchange rate for a currency pair. It also sets the exchange rate for the
        reversed pair.
        
        Parameters
        ----------
        base: str
            ISO code of the base currency
        quotation: str
            ISO code of the quotation currency
        rate: float
            Exchange rate for the currency pair
        
        Returns
        -------
        None
        """
        if base in self.Currencies and quotation in self.Currencies:
            self.ConversionTable[(base,quotation)]=rate
            self.ConversionTable[(quotation,base)]=1/rate
        else:
            raise KeyError("One of the currencies has not been found")
            
    def Convert(self,base,quotation,value):
        """
        Convert a value expressed in the base currency to a value expressed in the 
        quotation currency
        
        Parameters
        ----------
        base: str
            ISO code of the base currency
        quotation: str
            ISO code of the quotation currency
        value: float
            Value expressed in the base currency to convert to the base currency
            
        Returns
        -------
        type: float
            Value converted to the quotation currency
        """
        return value * self.ConversionTable[(base,quotation)]