# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 23:33:25 2017

@author: clem
"""

class SecurityManager:
    """
    Component of the workflow management responsible for the security management
    """
    def __init__(self):
        self.Securities = {}
        
    def AddSecurity(self,security):
        self.Securities[security.ISIN]=security
        
    def AddEconomicModel(self,econmodel):
        for isin,s in self.Securities.iteritems():
            econmodel.AddSecurity(s)
    
    def GetChangesOverview(self):
        tempdic = {}
        for isin,sec in self.Securities.iteritems():
            tempdic[isin]=[sec.GetRelativeChange(),sec.GetAbsoluteChange(),sec.Currency]
        return tempdic
    
    def _PrintChangesOverview(self):
        for isin,changetab in self.GetChangesOverview().iteritems():
            print("{0} - {1}% - {3}{2}".format(isin,100*changetab[0],changetab[1],changetab[2]))
    
    def __getitem__(self,isin):
        return self.Securities[isin]
        
    def __contains__(self,isin):
        return self.Securities.__contains__(isin)
        