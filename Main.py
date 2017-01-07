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

# Economic models
slr = SingleLeadingRate()
govlr = SingleLeadingRateByCurrency()


#Securities
bond1 = Security("FR123123",1,"EUR")
bond1.SetDuration(5)
bond2 = Security("CH123123",1,"CHF")
bond2.SetDuration(2)
bond3 = Security("US123123",1,"USD")
bond3.SetDuration(10)
bond4 = Security("US321098",1,"USD")
bond4.SetDuration(7)
secs = [bond1,bond2,bond3,bond4]

#Portofolios
p1 = Portfolio(1,"Discretionary")
p2 = Portfolio(2,"Non-discretionary","EUR")
pflio = [p1,p2]


#Workflow
monitor = MonitoringTool()

#Currencies
monitor.SetExchangeRate("EUR","USD",1.05)
monitor.SetExchangeRate("EUR","CHF",1.07)
monitor.SetExchangeRate("USD","CHF",1.02)

for s in secs:
    monitor._AddSecurity(s)

for p in pflio:
    monitor._AddPortfolio(p)

monitor._AddSecurityToPortfolio(1,"FR123123",1000)
monitor._AddSecurityToPortfolio(1,"CH123123",500)
monitor._AddSecurityToPortfolio(1,"US123123",1500)
monitor._AddSecurityToPortfolio(1,"US321098",300)
monitor._AddSecurityToPortfolio(2,"FR123123",500)
monitor._AddSecurityToPortfolio(2,"CH123123",1000)
monitor._AddSecurityToPortfolio(2,"US123123",1500)

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



