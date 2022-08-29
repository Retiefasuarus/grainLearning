# import matplotlib.pyplot as plt

# import numpy as np
# import pandas as pd

# import os
# import sys
# from pathlib import Path
# import unittest
# import numpy as np

# PROJECT_DIR = BASE_DIR = Path(os.path.abspath("")).resolve()

# MODULE_DIR = PROJECT_DIR.parent.parent

# print(MODULE_DIR)
# sys.path.insert(0, str(MODULE_DIR))

# import grainlearning as GL


# def test_param_config():
#     raw_config = {"ranges": {"E": [0, 100], "pois": [0.2, 0.4]}}
#     config = GL.ParametersConfig.from_dict(raw_config)

#     expected_config = GL.ParametersConfig(
#         names=["E", "pois"],
#         num_params=2,
#         mins=np.array([0.0, 0.2]),
#         maxs=np.array([100, 0.4]),
#         ranges={"E": [0, 100], "pois": [0.2, 0.4]},
#     )
#     np.testing.assert_equal(config.__dict__, expected_config.__dict__)


# def test_sim_config():

#     f = lambda obj: obj

#     raw_config = {"run_model": f, "num_samples": 10}
#     config = GL.SimulationConfig.from_dict(raw_config)

#     expected_config = GL.SimulationConfig(run_model=f, num_samples=10)
#     np.testing.assert_equal(config.__dict__, expected_config.__dict__)


# def test_obs_config():
#     control = np.random.normal(0, 1, 100) * 90
#     obs1 = np.random.normal(0, 1, 100)
#     obs2 = np.random.normal(0, 1, 100)

#     raw_config = {"data": obs1, "inv_obs_weight": [1], "control": control}
#     config = GL.ObservationsConfig.from_dict(raw_config)

#     expected_config = GL.ObservationsConfig(
#         data=np.array(obs1),
#         inv_obs_weight=[1],
#         num_observations=1,
#         num_steps=100,
#         control=control,
#     )

#     np.testing.assert_equal(config.__dict__, expected_config.__dict__)

#     # increase number of observables
#     raw_config = {"data": [obs1, obs2], "inv_obs_weight": [1]}
#     config = GL.ObservationsConfig.from_dict(raw_config)

#     expected_config = GL.ObservationsConfig(
#         data=np.array([obs1, obs2]),
#         inv_obs_weight=[1],
#         num_observations=2,
#         num_steps=100,
#     )

#     np.testing.assert_equal(config.__dict__, expected_config.__dict__)


# def test_dist_config():

#     raw_config = {"max_num_components": 2, "prior_weight": 0.5, "cov_type": "tied"}
#     config = GL.BayesianGaussianMixture.from_dict(raw_config)

#     expected_config = GL.BayesianGaussianMixture(
#         max_num_components=2, prior_weight=0.5, cov_type="tied"
#     )

#     np.testing.assert_equal(config.__dict__, expected_config.__dict__)

#     raw_config = {"max_num_components": 2}
#     config = GL.BayesianGaussianMixture.from_dict(raw_config)

#     expected_config = GL.BayesianGaussianMixture(
#         max_num_components=2, prior_weight=0.5, cov_type="full"
#     )

#     np.testing.assert_equal(config.__dict__, expected_config.__dict__)


# def test_smc_config():

#     raw_config = {
#         "sigma_guess": 2.0,
#         "ess_target": 0.5,
#         "sigma_min": 0.1,
#         "sigma_max": 2.0,
#         "scale_cov_with_max": False,
#     }
#     config = GL.SequentialMonteCarlo.from_dict(raw_config)

#     expected_config = GL.SequentialMonteCarlo(
#         sigma_guess=2.0,
#         ess_target=0.5,
#         sigma_min=0.1,
#         sigma_max=2.0,
#         scale_cov_with_max=False,
#     )

#     np.testing.assert_equal(config.__dict__, expected_config.__dict__)

#     raw_config = {
#         "sigma_guess": 2.0,
#         "ess_target": 0.5,
#     }
#     config = GL.SequentialMonteCarlo.from_dict(raw_config)

#     expected_config = GL.SequentialMonteCarlo(
#         sigma_guess=2.0,
#         ess_target=0.5,
#         sigma_min=1.0e-4,
#         sigma_max=1.0e6,
#         scale_cov_with_max=True,
#     )

#     np.testing.assert_equal(config.__dict__, expected_config.__dict__)


# def test_gl_config():

#     control = np.random.normal(0, 1, 100) * 90
#     obs1 = np.random.normal(0, 1, 100)
#     f = lambda obj: obj

#     raw_config = {
#         "observations": {"data": obs1, "control": control, "inv_obs_weight": [1]},
#         "simulations": {"run_model": f, "num_samples": 10},
#         "parameters": {"ranges": {"M": [0, 100], "C": [0.1, 0.4]}},
#     }


# test_param_config()
# test_sim_config()
# test_obs_config()
# test_dist_config()
# test_smc_config()
