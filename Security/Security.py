# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:27:30 2017

@author: clem
"""

class Security:
    
    """
    The Security class allows to store the information related to a fixed income security and perform 
    operation with it.
    
    Attributes of the Class
    -----------------------
    ISIN: str
        ISIN of the security (or unique identifier)
    MarketValue: float
        Market value per amount of nominal value.
    Currency: str
        Currency of the security
    PercentChange: float
        Relative change in price of the security
    Duration: float or Duration
        Value of duration, whether modified or key rate. If float, assumed to be modified duration
        
    Methods of the Class
    --------------------
    SetDuration:
        Set the duration
    _SetRelativeChange
        Set the relative change in value of the security for a given yield shock (called by YieldCurve
        instance)
    GetRelativeChange:
        Provide the relative change in value associated to the current yield shock (defined by the last
        economic model used)
    GetAbsoluteChange:
        Provide the absolute change in value associated to the current yield shock (defined by the last
        economic model used)
    
    
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
    
    def _SetRelativeChange(self,pc):
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