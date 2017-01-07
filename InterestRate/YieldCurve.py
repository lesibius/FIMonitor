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
        self.Securities = set()
    
    def SetYieldChangeRelationship(self,relationship):
        """
        Set the relationship governing the changes in the yield curve
        
        Parameters
        ----------
        relationship: function
            Function with the following form: None -> f(EconomicInputVariable(s),YieldCurve(s)) -> YieldChange instance        
        
        Returns
        -------
        None
        """
        self.Relationship = relationship
    
    def _SetYieldChange(self):
        self.YieldChange = self.Relationship()
        
    def AddSecurity(self,sec):
        self.Securities.add(sec)
        
    def PushSecurityRelativeChange(self):
        for sec in self.Securities:
            pc = self.YieldChange * sec.Duration
            sec._SetRelativeChange(pc)
    
    