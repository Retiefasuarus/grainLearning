# # %%

import numpy as np
import typing as t
from scipy import optimize
from .models import Model

from .sequentialmontecarlo import SequentialMonteCarlo

from .gaussianmixturemodel import GaussianMixtureModel

#  TODO add .from_dict class


class IterativeBayesianFilter:
    """Iterative Bayesian Filter class for probabalistic calibrations"""

    #: The inference class is a member variable of the particle filter which is used to generate the likelihood
    inference = t.Type["SequentialMonteCarlo"]

    #: The gaussian mixture model class is used to sample the parameters
    sampling = t.Type["GaussianMixtureModel"]

    #: This a tolarance to which the optimization algorithm converges.
    ess_tol: float = 1.0e-2

    #: this is the current proposal distribution
    proposal_ibf: np.ndarray

    #: This is the minimum value of sigma which is automatically adjusted such that to covariance matrix is not too big.
    sigma_min: float = 1.0e-6

    #: This is the maximum value of sigma which is automatically adjusted such that the covariance matrix is not singular
    sigma_max: float = 1.0e6

    def __init__(
        self,
        inference: t.Type["SequentialMonteCarlo"],
        sampling: t.Type["GaussianMixtureModel"],
        sigma_max: float = 1.0e6,
        sigma_min: float = 1.0e-6,
        ess_tol: float = 1.0e-2,
    ):
        """Initialize the Iterative Bayesian Filter class

        :param inference: Sequential Monte Carlo class (SMC)
        :param sampling: Gaussian Mixture Model class (GMM)
        :param sigma_max: Initial sigma max (this value gets automatically adjusted), defaults to 1.0e6
        :param sigma_min: Initial sigma min (this value gets automatically adjusted), defaults to 1.0e-6
        :param ess_tol: Tolarance for the effective sample size to converge, defaults to 1.0e-2
        """
        self.inference = inference
        self.sampling = sampling
        self.sigma_max = sigma_max
        self.sigma_min = sigma_min
        self.ess_tol = ess_tol
        self.proposal_ibf = None

    def set_proposal(self, model: t.Type["Model"]):
        """set the proposal distribution iterative bayesian filter

        :param model: Calibration model.
        :param input_proposal: initial proposal distribution, defaults to None
        """
        self.proposal_ibf = (
                np.ones([model.num_samples]) / model.num_samples
            )


    def check_sigma_bounds(
        self, sigma_adjust: float, model: t.Type["Model"]
    ):
        
        sigma_new = sigma_adjust
        while True:
            cov_matrices = self.inference.get_covariance_matrices(100, model)
            
            
            # print(sigma_new)
            # adjust_sigma_max = False
            # sigma_adjustment_factor = 1
            # for stp_id in range(model.observations.num_steps):
            #     covariant_matrix = self.inference.get_covariance_matrix(
            #         sigma_guess=sigma_new,
            #         observations=observations,
            #         load_step=stp_id,
            #     )
            #     if np.linalg.det(covariant_matrix) > 1e2:
            #         adjust_sigma_max = True
            #         sigma_adjustment_factor = 0.75
            #         break
            #     elif np.linalg.det(covariant_matrix) < 1e-7:
            #         adjust_sigma_max = True
            #         sigma_adjustment_factor = 1.75
            #         break

            # if adjust_sigma_max:
            #     sigma_new *= sigma_adjustment_factor
            # else:
            #     break
        # return sigma_new

    # @classmethod
    # def from_dict(cls: t.Type["IterativeBayesianFilter"], obj: dict):
    #     return cls(
    #         inference=SequentialMonteCarlo.from_dict(obj["inference"]),
    #         sigma_max=obj.get("sigma_max", 1.0e6),
    #         sigma_min=obj.get("sigma_min", 1.0e-6),
    #         ess_tol=obj.get("ess_tol", 1.0e-2),
    #         sampling=GaussianMixtureModel.from_dict(obj["sampling"]),
    #     )


#     def set_sigma_bounds(
#         self,
#         observations: t.Type["Observations"],
#     ):

#         self.sigma_min = self.check_sigma_bounds(
#             sigma_adjust=self.sigma_min, observations=observations
#         )

#         self.sigma_max = self.check_sigma_bounds(
#             sigma_adjust=self.sigma_max, observations=observations
#         )
#         assert self.sigma_min < self.sigma_max

#     def run_inference(
#         self, observations: t.Type["Observations"], simulations: t.Type["Model"]
#     ):
#         # reduce modeling error such that

#         result = optimize.minimize_scalar(
#             self.inference.data_assimilation_loop,
#             args=(self.proposal_ibf, observations, simulations),
#             method="bounded",
#             bounds=(self.sigma_min, self.sigma_max),
#         )
#         self.sigma_max = result.x


#         # make sure values are set
#         self.inference.data_assimilation_loop(
#             result.x, self.proposal_ibf, observations, simulations
#         )
#         self.proposal_ibf = self.inference.give_propsal()
#         print("proposal",self.proposal_ibf)
#         # print(self.sigma_min,self.sigma_max,self.proposal_ibf,result.x)

#     def run_sampling(self, simulations: t.Type["Model"]):
#         new_params = self.sampling.regenerate_params(self.proposal_ibf, simulations)
#         return new_params

#     def solve(
#         self, observations: t.Type["Observations"], simulations: t.Type["Model"]
#     ) -> np.ndarray:
#         self.run_inference(observations=observations, simulations=simulations)
#         new_params = self.run_sampling(simulations=simulations)
#         return new_params
