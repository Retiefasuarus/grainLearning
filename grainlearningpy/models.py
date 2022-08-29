#%%
from itertools import tee
import typing as t
import numpy as np
# import pandas as pd
from .parameters import Parameters
from .observations import Observations

class Model:
    """This is a base class which is used to call a user defined model. 
    
    It contains the parameters and the observations class.
    
    The number of samples, parameters and observations should be set first.
    
    Use this module like this:
    
    .. highlight:: python
    .. code-block:: python
    
        class MyModel(Model):
            parameters = Parameters(
                names=["k", "t"],
                mins=[100, 0.1],
                maxs=[300, 10],
            )
            observations = Observations(
                data=[100, 200, 300], ctrl=[-0.1, -0.2, -0.3], names=["F"], ctrl_name=["x"]
            )
            num_samples = 10

            def __init__(self):
                self.parameters.generate_halton(self.num_samples)

            def run(self):
                # for each parameter calculate the spring force
                data = []
                
                for params in self.parameters.data:
                    F = params[0]*params[1]*self.observations.ctrl
                    data.append(np.array(F,ndmin=2))
                    
                self.data = np.array(data)

    """

    #: Parameter class containing parameter data.
    parameters: t.Type["Parameters"]
    
    #: Observation class containing the reference data.
    observations: t.Type["Observations"]
    
    #: List of Pandas DataFrames containing the simulated data.
    data: np.array
    
    #: List of Pandas DataFrams contining the data records
    data_records: list[list[pd.DataFrame]] = []

    num_samples: int = 0
    #: Number of samples (usually specified by user)
    
    def run(self):
        """This function is called to populate the model"""
        pass
    
    def get_control_data(self)->pd.Series:
        """ Gets a Pandas Series of the control data. 
        
        This can be used in the simulations.

        :return: A Dataframe view containing only the
        """
        # Note slice(None) gives all content at that level
        return self.data.loc[:,self.observations.control]

    def get_key_data(self)->pd.DataFrame:
        """ Gets a Pandas DataFrame of the key data. 

        :return: A Dataframe view containing only the keys
        """
        return self.data.loc[:,self.observations.keys]
