import typing as t
import numpy as np

from scipy.stats import qmc


# TODO add so that the user can input a dataframe with initial parameters
class Parameters:
    """This class contains methods and information on the Simulation parameters.

        The mininum and maximum values must be specified for each parameters (e.g., `mins=[1e6,0.05,7.]` and `maxs=[4e7,1.,13.]`).
    """

    #: array containing the parameters.
    data: np.array

    #: The minimum values of the parameters.
    mins: list[float] = []

    #: The maximum values of the parameters.
    maxs: list[float] = []

    #: Names of the parameters.
    names: list[str]

    #: Number of parameters.
    num_params: int

    #: The data (Pandas Dataframes) of the previous calibration iterations.
    data_records: list = []

    def __init__(self, names: list[str], mins: list[float], maxs: list[float]):
        """Initialize the parameters class.

        :param names: The names of the parameters.
        :param mins: A list of containing the minimum values a parameter may have.
        :param maxs: A list of containing the maximum values a parameter may have.
        """
        self.names = names
        self.mins = mins
        self.maxs = maxs
        self.num_params = len(names)

    @classmethod
    def from_dict(cls: t.Type["Parameters"], obj: dict) -> t.Type["Parameters"]:
        """Create an Parameter class from a dictionary.

        Example:

        The input will look like this

        .. code-block:: json
        
            {
                "names": ["E", "Eta", "Psi"],
                "mins": [1e6,0.05,7.],
                "maxs": [4e7,1.0,13.],
            }

        :param cls: The Parameters class referenced to itself.
        :param obj: Dictionary containing the input parameters to the object.
        :return: An initialized Parameters object
        """#%%
        return cls(names=obj["names"], mins=obj["mins"], maxs=obj["maxs"])

    def generate_halton(self, num_samples: int):
        """Generate a Halton table of the parameters.

        :param num_samples: number of simulations
        """
        halton_sampler = qmc.Halton(self.num_params, scramble=False)
        param_table = halton_sampler.random(n=num_samples)

        for i in range(self.num_params):
            for j in range(num_samples):
                mean = 0.5 * (self.maxs[i] + self.mins[i])
                std = 0.5 * (self.maxs[i] - self.mins[i])
                param_table[j][i] = mean + (param_table[j][i] - 0.5) * 2 * std

        self.data = np.array(param_table,ndmin=2)
        self.data_records.append(self.data)