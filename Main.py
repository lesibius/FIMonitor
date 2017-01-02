# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:31:08 2017

@author: clem
"""

from Security import *
from Portfolio import *
from YieldCurve import *

yild1 = YieldCurve()
yild2 = YieldCurve()

yild1.SetYieldChange(0.007)
yild2.SetYieldChange(0.008)

somebond = Security("US123123",0.9937,"USD")
anotherbond = Security("CHF143543",1.134,"CHF")

somebond.SetDuration(5.0)
anotherbond.SetDuration(9.0)

somebond.SetYieldCurve(yild1)
anotherbond.SetYieldCurve(yild2)

p = Portfolio(1,"Managed accounts")

p.AddSecurity(somebond,1000)
p.AddSecurity(somebond,1000)
p.AddSecurity(anotherbond,1000)


print(p.GetMarketValue())

print(somebond.GetPercentLoss())

p.ComputeLoss("ADA")
for s,l in p.ScenarioLosses["ADA"].iteritems():
    print("{0}: {1}% - USD{2}".format(s.ISIN,100*l.Relative,l.Absolute))

l = p.ScenarioLosses["ADA"][somebond] + p.ScenarioLosses["ADA"][anotherbond]

print("{0}: {1}% - USD{2}".format(p.Description,100*l.Relative,l.Absolute))


yild1.SetYieldChange(0.001)
yild2.SetYieldChange(0.004)

p.ComputeLoss("ABA")
for s,l in p.ScenarioLosses["ABA"].iteritems():
    print("{0}: {1}% - USD{2}".format(s.ISIN,100*l.Relative,l.Absolute))

l = p.ScenarioLosses["ABA"][somebond] + p.ScenarioLosses["ABA"][anotherbond]

print("{0}: {1}% - USD{2}".format(p.Description,100*l.Relative,l.Absolute))