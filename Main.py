# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:31:08 2017

@author: clem
"""

from Workflow import *

from Security.Security import *
from SecurityGroup.Portfolio import *

from SimpleEconomicModels import *

slr = SingleLeadingRate()
govlr = SingleLeadingRateByCurrency()

bond1 = Security("FR123123",0.99,"EUR")
bond1.SetDuration(5)
bond2 = Security("CH123123",1.03,"CHF")
bond2.SetDuration(2)
bond3 = Security("US123123",0.98,"USD")
bond3.SetDuration(10)
bond4 = Security("US321098",0.97,"USD")
bond4.SetDuration(7)

p1 = Portfolio(1,"Discretionary")
p2 = Portfolio(2,"Non-discretionary")

secs = [bond1,bond2,bond3,bond4]
pflio = [p1,p2]
monitor = MonitoringTool()

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
print("\nShock 2:")
monitor.LoadInput("Single Leading Rate","Scenario 2",yieldshock=0.002)
slr.ApplyShock() 
monitor._PrintSecurityChangeOverview()
print("\nShock 3:")
govlr._LoadInput(**{"EUR":0.001,"USD":0.001,"CHF":0.002})
govlr.ApplyShock()
monitor._PrintSecurityChangeOverview()
print("\nShock 3:")
govlr._LoadInput(**{"EUR":0.001,"USD":0.01,"CHF":0.002})
govlr.ApplyShock()
monitor._PrintSecurityChangeOverview()