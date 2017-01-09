# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 19:56:55 2017

@author: clem
"""

from Portfolio import *

class AggregatedPortfolio(Portfolio):
    """
    The AggregatedPortfolio class allows combining Portfolio and other AggregatedPortfolio
    instances to compute aggregated measure of risk.
    
    It is a subclass of the Portfolio class.
    
    It works as dynamic composite: when calling the AggregateHoldings method of the class
    the holdings of all portfolios and sub-AggregatedPortfolio associated to the class
    are updated in the Holding attribute of the instance.
    
    Main Attributes
    ---------------
    See Portfolio class documentation.
    
    Main Methods
    ------------
    See Portfolio class documentation.
    
    Additional Methods
    ------------------
    AddPortfolio:
        Add a portfolio to the AggregatedPortfolio instance.
    AggregateHodldings:
        Update the self.Holdings attribute by aggregating this attribute for all Portfolio
        and sub-AggregatedPortfolio.
    
    """
    
    def __init__(self,aggregateID,description,reportingcurrency):
        """
        Constructor
        -----------
        
        Parameters
        ----------
        aggregateID: Any
            ID of the AggregatedPortfolio instance
        description: str
            Description of the AggregatedPortfolio instance
        reportingcurrency: str
            Reporting currency of the AggregatedPortfolio instance
            
        Returns
        -------
        type: AggregatedPortfolio
            A new AggregatedPortfolio instance
        """
        Portfolio.__init__(self,aggregateID,description,reportingcurrency)
        self.Portfolios = {}
        
    def AddPortfolio(self,portfolio):
        """
        Add a Portfolio instance to the AggregatedPortfolio instance
        
        Parameters
        ----------
        portfolio: Portfolio
            Portfolio instance to add to the AggregatedPortfolio instance        
        
        Returns
        -------
        None
        """
        self.Portfolios[portfolio.ID] = portfolio
        
            
    def AggregateHoldings(self):
        """
        Pull the holdings from each portfolios and sub-aggregated portfolios to this 
        AggregatedPortfolio instance.
        
        This method allows the AggregatedPortfolio class to work as dynamical composite.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        self.Holdings = {}      #Reinitialize self.Holdings
        for p in self.Portfolios.values():
           for sec,nomamount in p.Holdings.iteritems():
            self.AddSecurity(sec,nomamount) 
        