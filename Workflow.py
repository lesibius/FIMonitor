# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 19:22:50 2017

@author: clem
"""

from WorkflowComponent.EconomicModelManager import *
from WorkflowComponent.SecurityManager import *
        
class MonitoringTool:
    """
    Workflow manager of the monitoring tool
    """
    def __init__(self):
        self.SecurityManager = SecurityManager()
        self.Portfolios = {}
        self.EconomicModelManager = EconomicModelManager()
        
    def _AddSecurity(self,sec,override=False):
        """
        Add a Security instance to the workflow
        
        Parameters
        ----------
        sec: Security
            Security instance to add to the workflow
        override: bool
            False if ove
        """
        if (not sec.ISIN in self.SecurityManager) | override:
            self.SecurityManager.AddSecurity(sec)
            self.EconomicModelManager.AddSecurity(sec)
        else:
            raise Exception("Error when adding the security {0} in the workflow".format(sec.ISIN))
            
    def _AddPortfolio(self,portfolio,override=False):
        if (not portfolio.ID in self.Portfolios) | override:
            self.Portfolios[portfolio.ID]=portfolio
        else:
            raise Exception("Error when adding the portfolio {0} in the workflow".format(portfolio.ID))
            
    def _AddSecurityToPortfolio(self,pid,isin,nominalamount):
        self.Portfolios[pid].AddSecurity(self.SecurityManager[isin],nominalamount)
        
    def _AddEconomicModel(self,economicmodel,override=False):
        self.EconomicModelManager.AddEconomicModel(economicmodel,override)
        self.SecurityManager.AddEconomicModel(economicmodel)
    
    def _PrintSecurityChangeOverview(self):
        self.SecurityManager._PrintChangesOverview()
        
    def LoadInput(self,modelname,scenarioname,**kwargs):
        self.EconomicModelManager[modelname]._LoadInput(**kwargs)