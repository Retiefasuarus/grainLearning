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


# def test_init_toolbox():
#     sim_cls = GL.Simulations(num_samples=10)
#     obs_cls = GL.Observations(
#         data=[10, 20, 30, 40], control=[0, 1, 2, 3], inv_obs_weight=[1]
#     )
#     par_cls = GL.Parameters(names=["E", "pois"], mins=[1e5, 0.1], maxs=[1e7, 0.5])
#     smc_cls = GL.SequentialMonteCarlo(sigma_guess=10, ess_target=0.1)
#     gmm_cls = GL.GaussianMixtureModel(max_num_components=10)
#     ibf_cls = GL.IterativeBayesianFilter(smc_cls, gmm_cls)

#     toolbox_cls = GL.CalibrationToolbox(
#         simulations=sim_cls,
#         observations=obs_cls,
#         parameters=par_cls,
#         calibration=ibf_cls,
#     )

#     grainlearning_config = {
#         "simulations": {"num_samples": 10},
#         "observations": {
#             "data": [10, 20, 30, 40],
#             "control": [0, 1, 2, 3],
#         },
#         "parameters": {"names": ["E", "pois"], "mins": [1e5, 0.1], "maxs": [1e7, 0.5]},
#         "calibration": {
#             "inference": {"sigma_guess": 10, "ess_target": 0.1, "inv_obs_weight": [1]},
#             "distribution": {"max_num_components": 10},
#         },
#     }

#     toolbox_fb = GL.CalibrationToolbox.from_dict(grainlearning_config)

#     np.testing.assert_equal(
#         toolbox_fb.simulations.__dict__, toolbox_cls.simulations.__dict__
#     )
#     np.testing.assert_equal(
#         toolbox_fb.observations.__dict__, toolbox_fb.observations.__dict__
#     )
#     np.testing.assert_equal(
#         toolbox_fb.parameters.__dict__, toolbox_fb.parameters.__dict__
#     )
#     np.testing.assert_equal(
#         toolbox_fb.calibration.inference.__dict__,
#         toolbox_fb.calibration.inference.__dict__,
#     )
#     np.testing.assert_equal(
#         toolbox_fb.calibration.distribution.__dict__,
#         toolbox_fb.calibration.distribution.__dict__,
#     )
