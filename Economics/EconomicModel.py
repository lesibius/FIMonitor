# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 23:39:15 2017

@author: clem
"""

from EconomicInputVariable import *

class EconomicModel:
    """
    Class used to describbe economic models.
    
    As such, this class can be considered as "abstract".
    
    Main Attributes of the Class
    ----------------------------
    Name: str
        Name of the model. This value should be unique as it is used as a key in the workflow management
        of the monitoring tool.
    InputVariables: Dict(EconomicInputVariable)
        Dictionary of input variables used in the model. The name (Name attribute of EconomicInputVariable 
        instances) is used as the key for the dictionary.
    YieldCurves: Dict(YieldCurve)
        Dictionary of YieldCurve instances used to set the relative change in value of securities. Securities
        that relies on the model are usually stored within these YieldCurve instances.
    
    
    Common Methods to Subclasses
    ----------------------------
    SetNewInputVariable:
        Set a new input variable to the model
    AddSecurity:
        Add a Security instance to the economic model. Usually, this task is performed by adding the Security
        to one of the YieldCurve instance contained in the YieldCurves attribute of the EconomicModel class.
        Thus, an EconomicModel does not contain Security instances per se.
    ApplyShock:
        This method runs in two parts
        
        1) First, values of the change in the yield curves are pulled from the model through the relationships and input variables
        2) Then, the values of the change in the yield curves are pushed to the Security instance stored in the YieldCurve instances.
    
    Methods to Override in Subclasses
    ---------------------------------
    
    1) _ProvideYieldCurve
    2) _LoadInput
    
    Functionning
    ------------
    
    1) First set the input using the SetNewInputVariable method
    2) Then, add security to link input variables to ending yield curves
    3) Change the values of the input and run the model using the Run method
    """
    def __init__(self,name):
        self.Name = name
        self.InputVariables = {}        #Instances of input variable
        self.YieldCurves = {}           #End point yield curves
        
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
        type: list
            List with the following form: [isin,YieldCurve instance]
        """
        return self._ProvideYieldCurve(security)
    
    def _LoadInput(self,**kwargs):
        """
        Load a set of values for the input of the model
        
        Should be overrided for each implementation of the EconomicModel base class
        """
        raise NotImplementedError("The LoadInput method should be overrided for each class based on EconomicModel")
        
    
    def _ProvideYieldCurve(self,security):
        """
        Provide a yield curve to the security
        
        This method should be overrided in each model
        
        Parameters
        ----------
        security: Security
            Security to which a yield curve should be provided
        
        Returns
        -------
        Type: list
            List with the following form: [isin,YieldCurve instance]
            
        Warning
        -------
        When overriding this method, it is important to make sure that each instance of YieldCurve
        created should be added to the self.YieldCurves set
        """
        raise NotImplementedError()
        
    def ApplyShock(self):
        """
        Apply a yield shock to the Security instances added to the model
        
        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        for y in self.YieldCurves.values():
            y._SetYieldChange()
            y.PushSecurityRelativeChange()