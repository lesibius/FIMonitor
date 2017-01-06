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
                                            #Shape: {scenario name: **kwargs input}
        
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
        self._ProvideYieldCurve(security)
    
    def _LoadInput(self,*args,**kwargs):
        """
        Load a set of values for the input of the model
        
        Should be overrided for each implementation of the EconomicModel base class
        """
        raise NotImplementedError("The LoadInput method should be overrided for each class based on EconomicModel")
        
    
    def _ProvideYieldCurve(self,security):
        """
        Provide a yield curve to the security
        
        This method should be overrided in each model
        """
        raise NotImplementedError()