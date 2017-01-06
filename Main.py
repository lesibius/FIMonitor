# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:31:08 2017

@author: clem
"""

from Workflow import *
from SimpleEconomicModels import *

slr = SingleLeadingRate()

monitoring = MonitoringTool()

monitoring.AddEconomicModel(slr)


