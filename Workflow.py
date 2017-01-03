# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 18:41:22 2017

@author: clem
"""

from Portfolio import *
from Security import *
from YieldCurve import *

class Workflow:
    
    """
    Workflow management for the fixed income monitoring tool
    """    
    
    def __init__(self):
        self.Portfolios = {}
        self.Securities = {}
        self.EconomicModels = []
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
        Add a new Security instance to the workflow or override an existing Security instance (based on the isin)
        
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
        
    def AddSecurityToPortfolio(self,pid,isin,nomamount):
        try:
            self.Portfolios[pid].AddSecurity(self.Securities[isin],nomamount)
        except:
            raise Exception
    
    def SetNewEconomicModel(self,ecomodel):
        """
        Add an economic model to the workflow
        
        Parameters
        ----------
        ecomodel : EconomicModel
            Economic model to add to the workflow
            
        Returns
        -------
        None
        """
        self.EconomicModels.append(ecomodel)
    
    def RunAndCollectEconomicModel(self):
        """
        Run an economic models, remove it from the list of models and add it to the garbage
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        try:
            self.EconomicModels[0].Run()
            self.EconomicModelGarbage.append(self.EconomicModels[0])
        except:
            raise Exception
    
    def Run(self):
        """
        Run the whole workflow
        
        Parameters
        ---------
        None
        
        Returns
        -------
        None
        """
        self.RunAndCollectEconomicModel()
        