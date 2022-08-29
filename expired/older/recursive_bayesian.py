import numpy as np

class RecursiveBayesian:
    
    ips = None
    covs = None
    posterior = None
    likelihood = None
    proposal = None
    
    num_params = 0
    num_samples = 0

    def __init__(self,num_params,num_samples):
        self.num_samples = num_samples
        self.num_params = num_params
        self.ips = np.zeros([num_params, num_samples])
        self.covs = np.zeros([num_params, num_samples])
        self.posterior = np.zeros([num_params, num_samples])
        self.likelihood = np.zeros([num_params, num_samples])
    