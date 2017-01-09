# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 19:22:50 2017

@author: clem
"""

from WorkflowComponent.EconomicModelManager import *
from WorkflowComponent.SecurityManager import *
from SecurityGroup.CurrencyConverter import *
from SecurityGroup.AggregatedPortfolio import *
        
class MonitoringTool:
    """
    Workflow manager of the monitoring tool
    """
#####################################################################################
#                                   Constructor                                     #
#####################################################################################
    def __init__(self):
        self.SecurityManager = SecurityManager()
        self.Portfolios = {}
        self.EconomicModelManager = EconomicModelManager()
        self.CurrencyConverter = CurrencyConverter()
        
#####################################################################################
#                               Security Management                                 #
#####################################################################################
        
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
            self.CurrencyConverter.AddCurrency(sec.Currency)
        else:
            raise Exception("Error when adding the security {0} in the workflow".format(sec.ISIN))

#####################################################################################
#                               Portfolio Management                                #
#####################################################################################  
 
    def _AddPortfolio(self,portfolio,override=False):
        """
        Add a Portfolio to the monitoring tool
        
        Parameters
        ----------
        portfolio: Portfolio
            Portfolio instance to add to the monitoring tool
        override: bool
            If false, attempts to override an existing Portfolio will raise an exception
        """
        if (not portfolio.ID in self.Portfolios) | override:
            self.Portfolios[portfolio.ID]=portfolio
            self.CurrencyConverter.AddCurrency(portfolio.ReportingCurrency)
            portfolio.SetCurrencyConverter(self.CurrencyConverter)
        else:
            raise Exception("Error when adding the portfolio {0} in the workflow".format(portfolio.ID))
            
    def _AddSecurityToPortfolio(self,pid,isin,nominalamount):
        """
        Add a security (through its ISIN) to a portfolio (through its ID)
        
        Parameters
        ----------
        pid: Any
            ID of the Portfolio instance
        isin: str
            ISIN of the Security instance
        nominalamount: float
            Nominal amount (expressed in the currency of the security or as a quantity of security) held
            
        Returns
        -------
        None
        """
        self.Portfolios[pid].AddSecurity(self.SecurityManager[isin],nominalamount)

#####################################################################################
#                               Economic Model Management                           #
#####################################################################################

    def _AddEconomicModel(self,economicmodel,override=False):
        """
        Add an economic model to the monitoring tool
        
        Parmaters
        ---------
        economicmodel: EconomicModel
            EconomicModel instance to add to the monitoring tool
        override: bool
            If false, attempts to override an economic model will raise an exception
            
        Returns
        -------
        None
        """
        self.EconomicModelManager.AddEconomicModel(economicmodel,override)
        self.SecurityManager.AddEconomicModel(economicmodel)
        
    def LoadInput(self,modelname,scenarioname,**kwargs):
        """
        Load the input of an EconomicModel instance
        
        Parameters
        ----------
        modelname: str
            Name of the EconomicModel instance
        scenarioname: str
            Name of the scenario
        **kwargs
            Arguments (depends on the implementation of the EconomicModel abstract class)
            
        Returns
        -------
        None
        """
        self.EconomicModelManager[modelname]._LoadInput(**kwargs)

#####################################################################################
#                               Currency Management                                 #
#####################################################################################        
        
    def SetExchangeRate(self,base,quotation,rate):
        """
        Set the exchange rate for a currency pair
        
        Parameters
        ----------
        base: str
            Base currency
        quotation: str
            Quotation currency
        rate: float
            Exchange rate
        
        Returns
        -------
        None
        """
        try:
            self.CurrencyConverter.SetExchangeRate(base,quotation,rate)
        except KeyError:
            self.CurrencyConverter.AddCurrency(base)
            self.CurrencyConverter.AddCurrency(quotation)
            self.CurrencyConverter.SetExchangeRate(base,quotation,rate)
            
        
#####################################################################################
#                               Design Phase Methods                                #
#####################################################################################  
        
    def _PrintSecurityChangeOverview(self):
        """
        
        """
        self.SecurityManager._PrintChangesOverview()
        
    def _PrintPortfolio_(self):
        print("\n")
        for p in self.Portfolios.values():
            print("Portfolio: {0} - {1}".format(p.ID,p.Description))
            print("Market value:    {} {:5.2f}".format(p.ReportingCurrency,p.GetMarketValue()))
            print("Absolute change: {} {:5.2f}".format(p.ReportingCurrency,p.GetAbsoluteChange()))
            print("Relative change:    {:5.2f}%".format(100*p.GetRelativeChange()))
            print("Average duration: {:5.2f}".format(p.GetAverageDuration()))
            print("\n")