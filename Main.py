# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:31:08 2017

@author: clem
"""

from Security import *
from Portfolio import *

somebond = Security("US123123",0.9937,"USD")
anotherbond = Security("CHF143543",1.134,"CHF")

p = Portfolio(1,"Managed accounts")

p.AddSecurity(somebond,1000)
p.AddSecurity(somebond,1000)
p.AddSecurity(anotherbond,1000)


print(p.GetMarketValue())