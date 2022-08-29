import numpy as np

from .utilities import generate_halton


class SequentialMonteCarlo:

    ess_target = 0.0
    sigma_guess = 0.0
    sigma_min = 1.0e-4
    sigma_max = 1.0e6
    gle = 0.0  # grain learning absolute percentage error
    num_params = 0
    num_samples = 0
    num_observations = 0
    observation_ctrl_data = None

    scale_cov_with_max = False
    seed = 0

    ips = None
    covs = None
    posterior = None
    likelihood = None
    proposal = None

    num_loading_steps = 0
    param_names = []
    param_ranges = []
    param_samples = []  # old smc_samples

    observation_data = None
    simulation_data = None

    def __init__(
        self,
        sigma_guess,
        ess_target,
        num_samples,
        scale_cov_with_max=True,
        seed=0,
        sigma_min=1.0e-4,
        sigma_max=1.0e6,
    ):

        self.sigma_guess = sigma_guess
        self.ess_target = ess_target
        self.scale_cov_with_max = scale_cov_with_max
        self.seed = seed
        self.sigma_min = sigma_min
        self.sigma_max = sigma_max
        self.num_samples = num_samples
        # # move this to ML?
        # self.__max_num_components = 0
        self.__prior_weight
        # self.__cov_type = None

    def _set_inv_normalized_sigma(self):
        inv_obs_mat = np.diagflat(self.inv_obs_weight)
        self.inv_normalized_sigma = inv_obs_mat * np.linalg.det(inv_obs_mat) ** (
            -1.0 / inv_obs_mat.shape[0]
        )

    def _generate_params_from_halton(self):
        mins_maxs = np.array([self.param_ranges[name] for name in self.param_names])
        mins = mins_maxs[:, 0]
        maxs = mins_maxs[:, 1]
        generate_halton(self.num_params,self.num_samples,mins,maxs)
        

    def load_parameters(self, param_names, param_ranges, input_param_data=None):
        self.param_names = param_names
        self.param_ranges = param_ranges

        if input_param_data is not None:
            self.param_samples.append(input_param_data)
        else:
            self._generate_params_from_halton()
    
    def load_observations(self, input_data, inv_obs_weight):
        self.input_data = input_data
        self.inv_obs_weight = inv_obs_weight
        self.__set_inv_normalized_sigma()
        self.num_samples, self.num_observations = np.shape(input_data)

    #CalibrationToolBox
    def run(self):
        
        
        while True:
            # if proposal is None then use ghalton sequence
            self.parameters.draw_from_proposal(self.proposal) 
            
            # user defined function outside GL. Surrogate model can be added, anything can be done here :)
            self.simulations.run_model(self.parameters,self.callback) 
            
            self.posterior = self.smc.get_posterior( self.simulations,self.observation) # run ESS loop -> Recursive Bayesian
            
            if (self.sigma < self.tol):
                break
            
            self.proposal = self.gmm.get_proposal(self.posterior)
            
            