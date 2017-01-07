# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:34:49 2017

@author: clem
"""

import operator

class Portfolio:
    
    """
    Aggregation of Security instances with related methods
    """    
    
    def __init__(self,portfolioID,description,reportingcurrency = "USD"):
        
        """
        Constructor of the Portfolio class
        
        Parameters
        ----------
        portfolioID : any
            ID of the portfolio
        description : str
            Description of the portfolio
        reportingcurrency: str
            Reporting currency of the portfolio
            
        Returns
        -------
        A new Portfolio instance
        """
        
        self.ID = portfolioID
        self.Description = description
        self.Holdings = {}
        self.ScenarioLosses = {}
        self.ReportingCurrency = reportingcurrency
    
    
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
            tempMV = tempMV + self.CurrencyConverter.Convert(sec.Currency,self.ReportingCurrency,nomAmount * sec.MarketValue)
        return tempMV
        
    def GetAbsoluteChange(self):
        """
        Compute the absolute change in the market value of the Portfolio instance
        
        Parameters
        ----------
        None
        
        Returns
        -------
        type: float
            Absolute change in the market value of the Portoflio instance
        """
        tempChange = 0
        for sec,nomAmount in self.Holdings.iteritems():
            tempChange = tempChange + self.CurrencyConverter.Convert(sec.Currency,self.ReportingCurrency,nomAmount * sec.GetAbsoluteChange())
        return tempChange
    
    def GetRelativeChange(self):
        """
        Compute the relative change in the market value of the Portfolio instance
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        return self.GetAbsoluteChange() / self.GetMarketValue()
    
    def SetCurrencyConverter(self,converter):
        """
        Provides a currency convert to the Portfolio instance
        
        Parameters
        ----------
        converter: CurrencyConverter
            CurrencyConverter instance used to convert currencies within the Portfolio instance
            
        Returns 
        -------
        None
        """
        self.CurrencyConverter = converter
        
    def GetAverageDuration(self):
        """
        Compute the average duration of the portfolio
        
        If multiple currencies are present in the portoflio, market values of the positions 
        are converted to the reporting currency prior computing the average duration.
        
        Parameters
        ----------
        None
        
        Returns
        -------
        type: float
            Average duration of the portfolio
        """
        tempDuration = 0
        for sec,nomAmount in self.Holdings.iteritems():
            tempDuration = tempDuration + self.CurrencyConverter.Convert(sec.Currency,self.ReportingCurrency,sec.Duration * sec.MarketValue * nomAmount)
        return tempDuration/self.GetMarketValue()
        
    def GetRankedSecurities(self):
        """
        Provide a list of ISIN ranked by change in market value
        
        Parameters
        ----------
        None
        
        Returns
        -------
        type: list(str)
            List of ISIN ranked by change in market value
        """
        #First, get a dictionary {ISIN: change}
        tempdic = {sec: self.CurrencyConverter.Convert(sec.Currency,self.ReportingCurrency,self.Holdings[sec] * sec.MarketValue * sec.GetAbsoluteChange()) for sec in self.Holdings.keys()}
        return sorted(tempdic.items(), key=operator.itemgetter(1))