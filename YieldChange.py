# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 19:50:29 2017

@author: clem
"""

class YieldChange:
    
    """
    Class to record changes in the yield curve of an issuer/security
    """    
    
    def __init__(self,method = 'linear'):
        
        """
        Parameters
        ----------
        method: str
            Method used to interpolate between datapoints
        """
        self.Changes = {}
        
    def AddChange(self,maturity,change):
        """
        Add a datapoint to the YieldChange instance
        
        If the maturity is already present in the YieldChange instance, then it will be overrided        
        
        Parameters
        ----------
        maturity: float
            Maturity of the change (0 = today)
        change: float
            Value of the change for the given maturity
        
        Returns
        -------
        None
        """
        self.Changes[maturity] = change
        
    def SetChange(self,change):
        """
        Set the whole dataset at once
        
        If some datapoints are already present in the YieldChange instance, then they are deleted
        
        Parameters
        ----------
        change: dict
            Dictionary with the following form: {days to maturity: change in the yield curve}
        """
        self.Changes = change