# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 21:37:10 2017

@author: clem
"""

from Economics.EconomicModel import *
from Economics.EconomicInputVariable import *
from InterestRate.YieldCurve import *

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
        EconomicModel.__init__(self,"Single Leading Rate")
        self.LeadingRate = YieldCurve(ratedescription)
        self.RateName = ratename
        self.SetNewInputVariable(StateEconomicVariable(ratename,ratedescription))
        self.InputVariables[self.RateName].SetValue(self.LeadingRate)
        self.LeadingRate.SetYieldChangeRelationship(self._ChangeYield)
        self.YieldShock = 0
        self.YieldCurves[ratename] = self.LeadingRate
        
    def _ChangeYield(self):
        return self.YieldShock
        
              
    def _ProvideYieldCurve(self,security):
        #One yield curve for all securities
        self.InputVariables[self.RateName].Value.AddSecurity(security)
    
    def _LoadInput(self,yieldshock):
        self.YieldShock = yieldshock



class SingleLeadingRateByCurrency(EconomicModel):
    
    def __init__(self):
        EconomicModel.__init__(self,"Single Leading Rate by Currency")
        self.YieldChanges = {}
        
    def AddCurrency(self,currency):
        if not currency in self.YieldChanges.keys():
            def tempfun():
                return self.YieldChanges[currency]
            self.YieldCurves[currency] = YieldCurve("Government yield curve for {0}".format(currency))
            self.YieldCurves[currency].SetYieldChangeRelationship(tempfun)
            self.YieldChanges[currency] = 0
            self.InputVariables[currency]=self.YieldCurves[currency]
        else:
            raise Exception("Impossible to add {0} to {1} model".format(currency,self.Name))
    
    def GetCurrencies(self):
        return self.YieldCurves.keys
    
    def _ProvideYieldCurve(self,security):
        tempcur = security.Currency
        try:
            self.AddCurrency(tempcur)       #Try to add
        except:
            pass
        self.YieldCurves[tempcur].AddSecurity(security)
        
    def _SetYieldShock(self,currency,change):
        self.YieldChanges[currency] = change
    
    def _LoadInput(self,**kwargs):
        for cur,change in kwargs.iteritems():
            self._SetYieldShock(cur,change)
    
    