# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:31:08 2017

@author: clem
"""

from Workflow import *

from Security.Security import *
from SecurityGroup.Portfolio import *

from SimpleEconomicModels import *

from SecurityGroup.CurrencyConverter import *

import csv



# Economic models
slr = SingleLeadingRate()
govlr = SingleLeadingRateByCurrency()


#Workflow
monitor = MonitoringTool()

#Currencies
monitor.SetExchangeRate("EUR","USD",1.05)
monitor.SetExchangeRate("EUR","CHF",1.07)
monitor.SetExchangeRate("USD","CHF",1.02)

    
with open('Securities.csv','r') as csvfile:
    spamreader = csv.DictReader(csvfile,delimiter=',')
    for row in spamreader:
        tempsec = Security(row["ISIN"],float(row["Market Value"]),row["Currency"])
        tempsec.SetDuration(float(row["Duration"]))
        monitor._AddSecurity(tempsec)
    
with open('Portfolio.csv','r') as csvfile:
    spamreader = csv.DictReader(csvfile,delimiter=',')
    for row in spamreader:
        temppflio = Portfolio(row["Portfolios"],row["Description"],row["Currency"])
        monitor._AddPortfolio(temppflio)
        
with open('Holdings.csv','r') as csvfile:
    spamreader = csv.DictReader(csvfile,delimiter=',')
    for row in spamreader:
        monitor._AddSecurityToPortfolio(row["ID"],row["ISIN"],float(row["Amount"]))


monitor._AddEconomicModel(slr)
monitor._AddEconomicModel(govlr)

print("\nShock 1:")
monitor.LoadInput("Single Leading Rate","Scenario 1",yieldshock = 0.001)
monitor.EconomicModelManager["Single Leading Rate"].ApplyShock()   
monitor._PrintSecurityChangeOverview()
monitor._PrintPortfolio_()
print("\nShock 2:")
monitor.LoadInput("Single Leading Rate","Scenario 2",yieldshock=0.002)
slr.ApplyShock() 
monitor._PrintSecurityChangeOverview()
monitor._PrintPortfolio_()
print("\nShock 3:")
govlr._LoadInput(**{"EUR":0.001,"USD":0.001,"CHF":0.002})
govlr.ApplyShock()
monitor._PrintSecurityChangeOverview()
monitor._PrintPortfolio_()
print("\nShock4:")
govlr._LoadInput(**{"EUR":0.001,"USD":0.01,"CHF":0.002})
govlr.ApplyShock()
monitor._PrintSecurityChangeOverview()
monitor._PrintPortfolio_()


secranking = monitor.Portfolios["A"].GetRankedSecurities()
for s in secranking:
    print("{} - {:5.2f}".format(s[0].ISIN,s[1]))
print("\n")

"""
secranking = monitor.Portfolios[2].GetRankedSecurities()
for s in secranking:
    print("{} - {:5.2f}".format(s[0].ISIN,s[1]))
"""

ap = AggregatedPortfolio("12","Company","USD")
ap.SetCurrencyConverter(monitor.CurrencyConverter)
ap.AddPortfolio(monitor.Portfolios["A"])
ap.AddPortfolio(monitor.Portfolios["F"])
ap.AggregateHoldings()
print(ap.Holdings)
secranking = ap.GetRankedSecurities()
for s in secranking:
    print("{} - {:5.2f}".format(s[0].ISIN,s[1]))
print(ap.GetRelativeChange())

