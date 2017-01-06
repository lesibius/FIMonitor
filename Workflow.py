# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 19:22:50 2017

@author: clem
"""

class EconomicModelManager:
    
    def __init__(self):
        self.EconomicModels = {}
        
    def AddEconomicModel(self,ecomodel):
        if not ecomodel.Name in self.EconomicModels:
            self.EconomicModels[ecomodel.Name]=ecomodel
        else:
            raise Exception("The economic model {0} is already present in the workflow".format(ecomodel.Name))
class PortfolioManager:
    
    def __init__(self):
        self.Portfolios = {}

class SecurityManager:
    
    def __init__(self):
        self.Securities = {}
        
    def AddEconomicModel(self,ecomodel):
        
        for isin,s in self.Securities.iteritems():
            ecomodel.AddSecurity(s)
        
        
class MonitoringTool:
    
    def __init__(self):
        self.EconomicModelManager = EconomicModelManager()
        self.PortfolioManager = PortfolioManager()
        self.SecurityManager = SecurityManager()
    
    def AddSecurity(self,security):
        self.SecurityManager.AddSecurity(security)
        self.EconomicModelManager.AddSecurity(security)
    
    def AddEconomicModel(self,economicmodel):
        self.EconomicModelManager.AddEconomicModel(economicmodel)
        self.SecurityManager.AddEconomicModel(economicmodel)
        
    def AddSecurityToPortfolio(self,isin,pid,nominalamount):
        self.PortfolioManager.AddSecurityToPortfolio(isin,pid,nominalamount)
        
    def LoadInput(self,ecomodelname,*args,**kwargs):
        self.EconomicModelManager.EconomicModels[ecomodelname]._LoadInput(args,kwargs)