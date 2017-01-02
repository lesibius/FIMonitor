# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:27:30 2017

@author: clem
"""

class Security:
    
    """
    The Security class allows to store the information related to a fixed income security
    """    
    
    def __init__(self,isin,mv,currency):
        
        """
        Constructor of the class
        
        Parameters
        ----------
        isin : str
            ISIN of the security
        mv : float
            Current market value by nominal amount the security
        currency : str
            Currency used to express the value of the security
            
        Returns
        -------
        
        A new instance of Security
        
        """        
        
        self.ISIN = isin
        self.MarketValue = mv