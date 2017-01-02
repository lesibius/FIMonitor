# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:34:49 2017

@author: clem
"""

class Portfolio:
    
    """
    Aggregation of Security instances with related methods
    """    
    
    def __init__(self,portfolioID,description):
        
        """
        Constructor of the Portfolio class
        
        Parameters
        ----------
        portfolioID : any
            ID of the portfolio
        description : str
            Description of the portfolio
            
        Returns
        -------
        A new Portfolio instance
        """
        
        self.ID = portfolioID
        self.Description = description
        self.Holdings = {}
        
    def AddSecurity(self,sec,nomAmount):
        
        """
        Add a Security instance with its related nominal amount to the portfolio.
        If the Security instance is already present in the portfolio, the nominal amount is increased
        
        Parameters
        ----------
        sec : Security
            Security instance to add to the porfolio
        nomAmount:
            Nominal quantity of the Security in the Portfolio
            
        Returns
        -------
        type: bool
            True if the Security was already present,
            False otherwise
        
        """        
        
        try:
            self.Holdings[sec] = self.Holdings[sec] + nomAmount
            return True
        except KeyError as ke:
            self.Holdings[sec] = nomAmount
            return False
            
    def GetMarketValue(self):
        
        """
        Compute the market value of the portfolio
        
        Warning
        -------
        Multiple currencies computation is currently not supported
        
        Parameters
        ----------
        None
        
        Returns
        -------
        type : float
            The market value of the portfolio, based on the nominal value and market value per unit of the securities
        
        """        
        
        tempMV = 0
        for sec, nomAmount in self.Holdings.iteritems():
            tempMV = tempMV + nomAmount * sec.MarketValue
        return tempMV
        