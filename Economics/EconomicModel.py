# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 23:39:15 2017

@author: clem
"""

from EconomicInputVariable import *

class EconomicModel:
    """
    Class responsible for the management of economic models
    
    As such, this class can be considered as "abstract"
    
    Functionning
    ------------
    
    1) First set the input using the SetNewInputVariable method
    2) Then, add security to link input variables to ending yield curves
    3) Change the values of the input and run the model using the Run method
    """
    def __init__(self):
        self.InputVariables = {}        #Instances of input variable
        self.InputValueSet = {}         #Dictionary used to fill input variables
                                            #Shape: {scenario name: {InputVariable name: value}}
        self.YieldCurves = set()
        
    def SetNewInputVariable(self,inputvariable):
        """
        Add a new input variable
        
        If an input variable with the same name is already present in the model, then it will
        be overrided
        
        Parameters
        ----------
        
        inputvariable: EconomicInputVariable
            Economic input variable to append
        Returns
        -------
        
        None
        """
        self.InputVariables[inputvariable.Name]=inputvariable
        
    def AddSecurity(self,security):
        """
        Add a security to the model by providing it a yield curve
        
        This method requires to override the _ProvideYieldCurve method        
        
        Parameters
        ----------
        security: Security
            Security to add to the the model
            
        Returns
        -------
        None
        """
        self._ProvideYieldCurve(security)
    
    def _LoadInput(self,scenarioname,*args,**kwargs):
        """
        Load a set of values for the input of the model
        
        Should be overrided for each implementation of the EconomicModel base class
        """
        raise NotImplementedError("The LoadInput method should be overrided for each class based on EconomicModel")
        
    
    def _ProvideYieldCurve(self,security):
        """
        Provide a yield curve to the security
        
        This method should be overrided in each model
        
        Warning
        -------
        When overriding this method, it is important to make sure that each instance of YieldCurve
        created should be added to the self.YieldCurves set
        """
        raise NotImplementedError()
        
    def Run(self,scenarioname):
        """
        Run the model using a scenario name
        
        Parameters
        ----------
        scenarioname: str
            Name of the scenario used to run the model
            
        Returns
        -------
        None
        """
        for inputname,value in self.InputValueSet.iteritems():
            self.InputVariables[inputname].SetValue(value)
        
        for yc in self.YieldCurves:
            yc.GetYieldChange()