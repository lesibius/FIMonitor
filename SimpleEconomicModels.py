# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 21:37:10 2017

@author: clem
"""

from EconomicModel import *
from EconomicInputVariable import *
from YieldCurve import *
from Security import *

class SingleLeadingRate(EconomicModel):
    """
    Economic model that use a single rate to model the economy.
    
    Description
    -----------
    
    This model use a single interest rate to model the whole economy. it results in a single shock
    for every instruments. The difference in losses between assets comes from internal characteristics
    of the fixed income instruments, as well as the exposure
    
    Use
    ---
    
    After creating an instance of the class:
    
    1) Call the 
    
    NB: when creating a new instance, it is possible to provide a name and description to the
    leading rate for reporting purposes
    
    Rationale
    ---------
    
    This model is best suited for portfolios consisting of treasury fixed income instruments in 
    one currency, from a single issuer, with similar characteristics (e.g. same covenants).
    It allows to quickly define a model for such simple portofolios. However, it suffers a lot
    of drawbacks (see "limitations" thereafter)
    
    Limitations
    -----------
    
    1) This model is useful if all securities in the scope are exposed to the same yield curve
    2) Different currencies implies different yield curve, and as such, this model cannot handle this situation
    
    
    """
    def __init__(self,ratename = "Leading interest rate",ratedescription = "Leading interest rate"):
        """
        Parameters
        ----------
        ratename: str
            Name of the leading interest rate
        ratedescription: str
            Description of the leading interest rate
        """
        EconomicModel.__init__(self)
        self.RateName = ratename
        self.SetNewInputVariable(StateEconomicVariable(ratename,ratedescription))
        self.InputVariables[self.RateName].SetValue(YieldCurve(ratedescription))
        self.InputVariables[self.RateName].Value.SetYieldChangeRelationship(self._ChangeYield)
        self.YieldShock = 0
        
    def _ChangeYield(self):
        return self.YieldShock
        
    def ApplyShock(self,yieldshock):
        self.YieldShock = yieldshock
        self.InputVariables[self.RateName].Value._SetYieldChange()
        
              
    def _ProvideYieldCurve(self,security):
        #One yield curve for all securities
        security.SetYieldCurve(self.InputVariables[self.RateName].Value)
        