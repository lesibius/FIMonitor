# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 12:11:13 2017

@author: clem
"""

class YieldCurve:
    
    """
    Basis class to operate with yields
    """    
    
    def __init__(self,description = None):
        
        """
        Constructor of the YieldCurve class
        
        Parameters
        ----------
        description: str
            Description of the yield curve
            
        Returns
        -------
        type: YieldCurve
            A new YieldCurve instance
        """        
        
        self.Description = description
        
    def SetYieldChange(self,yc):
        self.YieldChange = yc