# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:31:08 2017

@author: clem
"""

from Workflow import *

wf = Workflow()

wf.SetNewSecurity("US123123",0.9937,"USD",5.0)
wf.SetNewSecurity("CHF143543",1.134,"CHF",9.0)

wf.SetNewPortfolio(1,"Managed Accounts")
wf.SetNewPortfolio(2,"Execution Only")


wf.AddSecurityToPortfolio(1,"US123123",1000)
wf.AddSecurityToPortfolio(1,"CHF143543",1000)

wf.AddSecurityToPortfolio(2,"US123123",500)
wf.AddSecurityToPortfolio(2,"CHF143543",1500)

wf.SetNewEconomicModel("Single rate model",SingleLeadingRate())
wf.SetNewSecurity("FR123123",1.0,"CHF",1.32)

wf.AddSecurityToPortfolio(1,"FR123123",231)

#wf.Run('Single rate model',1)

