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
        self.PercentChange = 0
        self.Currency = currency
    
    def SetDuration(self,duration):
        
        """
        Set the duration for the Security instance
        
        Parameters
        ----------
        duration : Duration
            Duration instance associated to the Security instance
        """
        self.Duration = duration
    
    def SetRelativeChange(self,pc):
        """
        Set the percent change of the Security instance
        
        Parameters
        ----------
        pc: float
            Change as a percentage of the market value        
        
        Returns
        -------
        None
        """
        self.PercentChange = pc
        
    def GetRelativeChange(self):
        
        """
        Return the change as percentage of the market value
        
        Parameters
        ----------
        None
        
        Returns
        -------
        type : float
            Change as a percentage of the market value of the Security instance
        """
        return self.PercentChange
        
    def GetAbsoluteChange(self):
        """
        Returns the absolute change per nominal amount
        
        Parameters
        ----------
        None
        
        Returns
        -------
        type: float
            Change per nominal amount of the market value of the Security instance
        """
        return self.PercentChange * self.MarketValue