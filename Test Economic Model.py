# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 21:32:13 2017

@author: clem
"""

from SimpleEconomicModels import *

Bond1 = Security("AAA",1,"USD")
Bond2 = Security("BBB",0.99,"USD")
Bond3 = Security("CCC",1.1,"USD")

p = [Bond1,Bond2,Bond3]

Bond1.SetDuration(2)
Bond2.SetDuration(3)
Bond3.SetDuration(5)



sem = SingleLeadingRate("US rate","2Y rate of the US Treasury")
sem.AddSecurity(Bond1)
sem.AddSecurity(Bond2)
sem.AddSecurity(Bond3)

sem.ApplyShock(12)

for b in p:
    print(b.GetPercentLoss())

sem.ApplyShock(100)
for b in p:
    print(b.GetPercentLoss())