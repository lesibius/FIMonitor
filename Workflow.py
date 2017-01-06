# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 18:41:22 2017

@author: clem
"""

from FinUtil.Portfolio import *
from FinUtil.Security import *
from InterestRate.YieldCurve import *
from Economics.EconomicModel import *
from SimpleEconomicModels import *

class Workflow:
    
    """
    Workflow management for the fixed income monitoring tool
    """    
    
    def __init__(self):
        self.Portfolios = {}
        self.Securities = {}
        self.EconomicModels = {}
        self.EconomicModelGarbage = []
        
    def SetNewPortfolio(self,pid,description = None):
        
        """
        Add a new Portfolio instance to the workflow or override an existing Portfolio instance (based on the id)
        
        Parameters
        ----------
        pid : str
            ID of the portfolio
        description : 
            Description of the portfolio
        """
        
        self.Portfolios[pid] = Portfolio(pid,description)
        
    def SetNewSecurity(self,isin,mv,currency,duration):
        
        """
        Add a new Security instance to the workflow or override an existing Security 
        instance (based on the isin)
        
        If economic models have been added to the workflow, the new security is linked to the
        model
        
        Parameters
        ----------
        isin: str
            ISIN of the security
        mv : float
            Market value of the security
        currency : str
            Currency used to express the market value of the security
        duration : Duration
            Duration instance associated to the Security instance
            
        Returns
        -------
        None
        """
        self.Securities[isin] = Security(isin,mv,currency)
        self.Securities[isin].SetDuration(duration)
        
        if self.EconomicModels:
            for n,e in self.EconomicModels.iteritems():
                e.AddSecurity(self.Securities[isin])
        
    def AddSecurityToPortfolio(self,pid,isin,nomamount):
        try:
            self.Portfolios[pid].AddSecurity(self.Securities[isin],nomamount)
        except:
            raise Exception()
    
    def SetNewEconomicModel(self,name,ecomodel):
        """
        Add an economic model to the workflow
        
        If securities have been added to the workflow, then they are integrated to the model
        
        Parameters
        ----------
        ecomodel : EconomicModel
            Economic model to add to the workflow
            
        Returns
        -------
        None
        """
        self.EconomicModels[name]=ecomodel
        if self.Securities:
            for isin,s in self.Securities.iteritems():
                ecomodel.AddSecurity(s)
                
    def Run(self,modelname,inputversion):
        #test
        self.EconomicModels[modelname].LoadInput()
    
    
        