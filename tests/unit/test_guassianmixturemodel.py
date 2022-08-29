# import matplotlib.pyplot as plt

# import numpy as np
# import pandas as pd

# import os
# import sys
# from pathlib import Path

# import numpy as np

# PROJECT_DIR = BASE_DIR = Path(os.path.abspath("")).resolve()

# MODULE_DIR = PROJECT_DIR.parent.parent

# print(MODULE_DIR)
# sys.path.insert(0, str(MODULE_DIR))

# import grainlearning as GL

# def test_init_gmm():
#     gmm = GL.GaussianMixtureModel(10)

#     assert isinstance(
#         gmm, GL.GaussianMixtureModel
#     ), "GMM is not instance of GaussianMixtureModel"

#     assert gmm.prior_weight == 0.1, "GMM prior weight not as expected"



# def test_init():
#     gmm_cls = GaussianMixtureModel(max_num_components=5)

#     assert isinstance(gmm_cls, GaussianMixtureModel)

#     gmm_dct = GaussianMixtureModel.from_dict({"max_num_components": 5})

#     np.testing.assert_equal(gmm_dct.__dict__, gmm_cls.__dict__)

#     assert gmm_cls.prior_weight == 1.0 / 5


# def test_expand_proposal_to_normalized_params():
#     proposal = np.array([0.25, 0.25, 0.25, 0.25])

#     sim = Simulations.from_dict(
#         {
#             "num_samples": 4,
#             "parameters": {
#                 "names": ["E", "pois"],
#                 "mins": [1e6, 0.19],
#                 "maxs": [1e7, 0.5],
#             },
#         }
#     )

#     sim.parameters.generate_halton(num_samples=sim.num_samples)

#     gmm_cls = GaussianMixtureModel(max_num_components=5, expand_weight=1)

#     expanded_parms,max_params = gmm_cls.expand_weighted_parameters(proposal, sim)

#     np.testing.assert_almost_equal(np.amax(expanded_parms, axis=0), np.ones(2))
#     # print(expanded_parms)
#     np.testing.assert_array_almost_equal(
#         expanded_parms,
#         np.array(
#             [
#                 [0.12903226, 0.4789916],
#                 [0.12903226, 0.4789916],
#                 [0.70967742, 0.7394958],
#                 [0.70967742, 0.7394958],
#                 [0.41935484, 1.0],
#                 [0.41935484, 1.0],
#                 [1.0, 0.56582633],
#                 [1.0, 0.56582633],
#             ]
#         ),
#         0.0001,
#     )


# def test_regenerate_params():
#     proposal = np.array([0.25, 0.25, 0.25, 0.25])

#     sim = Simulations.from_dict(
#         {
#             "num_samples": 4,
#             "parameters": {
#                 "names": ["E", "pois"],
#                 "mins": [1e6, 0.19],
#                 "maxs": [1e7, 0.5],
#             },
#         }
#     )

#     sim.parameters.generate_halton(num_samples=sim.num_samples)

#     gmm_cls = GaussianMixtureModel(max_num_components=2, expand_weight=1)

#     expanded_params = gmm_cls.regenerate_params(proposal, sim)

#     assert np.all(expanded_params > np.array(sim.parameters.mins))
#     assert np.all(expanded_params < np.array(sim.parameters.maxs))