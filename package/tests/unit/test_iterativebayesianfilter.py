import numpy as np

from grainlearning import SequentialMonteCarlo, IterativeBayesianFilter


def test_init():
    smc_cls = SequentialMonteCarlo(ess_target=0.1, inv_obs_weight=[1])

    ibf_cls = IterativeBayesianFilter(smc_cls, sigma_max=2)

    ibf_dct = IterativeBayesianFilter.from_dict(
        {"inference": {"ess_target": 0.1, "inv_obs_weight": [1]}, "sigma_max": 2}
    )

    assert isinstance(ibf_cls, IterativeBayesianFilter)

    raw_ibf_dct = ibf_dct.__dict__
    raw_ibf_cls = ibf_cls.__dict__

    raw_ibf_dct.pop("inference")
    raw_ibf_cls.pop("inference")

    np.testing.assert_equal(raw_ibf_dct, raw_ibf_cls)


# def test_set_proposal():

#     smc_cls = GL.SequentialMonteCarlo(ess_target=0.1, inv_obs_weight=[1])

#     ibf_cls = GL.IterativeBayesianFilter(smc_cls, sigma_max=2)

#     sims = GL.Simulations.from_dict(
#         {
#             "num_samples": 2,
#             "parameters": {
#                 "names": ["E", "pois"],
#                 "mins": [1e7, 0.1],
#                 "maxs": [1e8, 0.7],
#             },
#         }
#     )

#     ibf_cls.set_proposal(simulations=sims)

#     np.testing.assert_equal(ibf_cls.proposal_ibf, np.array([0.5, 0.5]))
#     ibf_cls.set_proposal(simulations=sims, input_proposal=np.array([0.2, 0.2]))
#     np.testing.assert_array_almost_equal(ibf_cls.proposal_ibf, np.array([0.2, 0.2]))


# def test_check_sigma_bounds():
#     smc_cls = GL.SequentialMonteCarlo(ess_target=0.1, inv_obs_weight=[1, 1])

#     ibf_cls = GL.IterativeBayesianFilter(smc_cls, sigma_max=2)

#     obs = GL.Observations(data=[[1, 1, 1, 1], [2, 2, 2, 2]], control=[[1, 2, 3, 4]])

#     sigma_high = ibf_cls.check_sigma_bounds(1e10, obs)

#     assert sigma_high < 300

#     sigma_low = ibf_cls.check_sigma_bounds(1e-10, obs)

#     assert sigma_low > 0.006


# def test_solve():
#     smc_cls = GL.SequentialMonteCarlo(ess_target=0.5, inv_obs_weight=[1, 1])

#     ibf_cls = GL.IterativeBayesianFilter(smc_cls)

#     sims = GL.Simulations.from_dict(
#         {
#             "num_samples": 10,
#             "parameters": {
#                 "names": ["E", "pois"],
#                 "mins": [1e7, 0.1],
#                 "maxs": [1e8, 0.7],
#             },
#         }
#     )

#     sims.parameters.generate_halton(sims.num_samples)

#     sims.state = np.array(
#         [
#             [[0, 2, 6, 0], [7, 4, 3, 7]],
#             [[9, 4, 5, 3], [1, 1, 5, 0]],
#             [[2, 9, 6, 5], [4, 1, 6, 3]],
#             [[5, 3, 4, 1], [3, 4, 3, 7]],
#             [[7, 4, 8, 7], [7, 0, 1, 7]],
#             [[6, 8, 7, 0], [6, 6, 7, 4]],
#             [[9, 3, 5, 6], [2, 6, 3, 8]],
#             [[4, 2, 1, 5], [2, 1, 0, 7]],
#             [[5, 9, 0, 9], [2, 6, 1, 9]],
#             [[5, 9, 9, 7], [2, 9, 3, 6]],
#         ]
#     )

#     ibf_cls.set_proposal(sims)

#     obs = GL.Observations(data=[[5, 6, 1, 3], [4, 9, 4, 5]], control=[[1, 2, 3, 4]])

#     ibf_cls.set_sigma_bounds(obs)

#     sigma_max_old = ibf_cls.sigma_max

#     ibf_cls.solve(obs, sims)

#     print(ibf_cls.proposal_ibf)
#     np.testing.assert_almost_equal(sum(ibf_cls.proposal_ibf), 1.0, 0.00001)

#     print(ibf_cls.sigma_max, sigma_max_old)
#     assert sigma_max_old > ibf_cls.sigma_max


# test_solve()
# #%%
# import numpy as np
# import matplotlib.pyplot as plt

# proposal = np.array(
#     [
#         1.28447963e-04,
#         8.91039254e-04,
#         1.04255693e-03,
#         9.24660880e-01,
#         2.01900929e-06,
#         1.98975435e-02,
#         1.98975435e-02,
#         2.02477872e-02,
#         1.30895571e-02,
#         1.42625063e-04,
#     ]
# )

# # plt.bar(np.arange(len(proposal)),proposal)

# new_proposal = np.random.choice(10,p=proposal)

# plt.bar(np.arange(len(proposal)),new_proposal)


# # %%
