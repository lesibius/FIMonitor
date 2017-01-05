# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 17:22:18 2017

@author: clem
"""

class EconomicInputVariable:
    
    """
    Input variable for economic models
    
    This class is an "abstract" class and cannot be used directly. It should be implemented through one of the following:
    
    1)StateEconomicVariable: for independant variable (use SetValue method)
    2)DependantEconomicVariable: for dependant variable (use SetEconomicRelationship method)
    """    
    
    def __init__(self,name,description):
        
        """
        Parameters
        ----------
        name : str
            Name of the variable
        description : str
            Description of the variable
        """
        self.Name = name
        self.Description = description
    
        
    def GetValue(self):
        """
        Returns the value of the variable
        
        Parameters
        ----------
        None
        
        Returns
        -------
        type: object
            Value of the economic variable
        """
        return self.Value

class StateEconomicVariable(EconomicInputVariable):
    
    """
    Input variable for economic model.
    
    Use this class for state (i.e. independant) variables
    """
    
    def SetValue(self,value):
        
        """
        Set the value of the variable
        
        Parameters
        ----------
        value : any
            Value of the variable
            
        Returns
        -------
        None
        """        
        self.Value = value

class DependantEconomicVariable(EconomicInputVariable):
    """
    Input variable for economic model.
    
    Use this class when the variable is not a variable state (i.e. it is dependant from other variable)
    """
    def SetEconomicRelationship(self,relationship):
        """
        Set the relationship between variables
        
        Parameters
        ----------
        relationship : function
            Function with the following form: None -> Object
        """
        self.Relationship = relationship
        
    def GetValue(self):
        #Overrided method
        return self.Relationship()