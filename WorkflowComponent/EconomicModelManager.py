# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 23:11:49 2017

@author: clem
"""

class EconomicModelManager:
    """
    Component of the worklow management responsible for the management of economic models
    
    Description
    -----------
    The economic model class is part of the global workflow management of the fixed income monitoring
    tool. It allows adding economic models (EconomicModel instance) to the workflow and help
    managing the addition/deletion of economic models and linking them with securities (Security instance)
    in the workflow.
    
    It contains a __getitem__ special method which allows retrieving quickly an EconomicModel 
    through its name.    
    
    Main Methods
    ------------
    AddEconomicModel:
        Add an EconomicModel instance to the manager
    AddSecurity:
        Add a Security instance to the EconomicModel instances stored in the manager
        
    Warning
    -------
    While the LoadInit method requires a scenario name, the management of pre-recorded scenario
    is not implemented yet.
    
    """
    def __init__(self):
        self.EconomicModels = {}    
        
    def AddEconomicModel(self,economicmodel,override):
        """
        Add an economic model to the workflow
        
        Parameters
        ----------
        economicmodel: EconomicModel
            EconomicModel instance to add to the workflow. Unique characteristics (i.e.
            methods and attributes that are not shared among EconomicModel subclassses) 
            of the model can be set prior to add the model to the workflow, or after by 
            accessing it through the __getitem__ method.
        override: bool
            If false, attempts to override a model already included in the workflow will raise
            an exception
            
        Returns
        -------
        None
        """
        if (not economicmodel in self.EconomicModels) | override:
            self.EconomicModels[economicmodel.Name]=economicmodel
        else:
            raise Exception("Error when adding the economic model {0} in the workflow".format(economicmodel.Name))
    
    def AddSecurity(self,sec):
        """
        Add a Security instance to each models in the workflow
        
        Parameters
        ----------
        sec: Security
            Security to add to the EconomicModel instances
        
        Returns
        -------
        None
        """
        for n,e in self.EconomicModels:
            e.AddSecurity(sec)
            
    def __getitem__(self,modelname):
        """
        Override the __getitem__ special method
        
        Parameters
        ----------
        modelname: str
            Name of the model to return
            
        Returns
        -------
        type: EconomicModel
            EconomicModel instance named modelname
        """
        return self.EconomicModels[modelname]