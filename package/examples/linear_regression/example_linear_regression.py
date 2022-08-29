import numpy as np
import pandas as pd

import os
import sys
from pathlib import Path

import numpy as np

PROJECT_DIR = BASE_DIR = Path(os.path.abspath("")).resolve()

MODULE_DIR = PROJECT_DIR.parent

print(MODULE_DIR)
sys.path.insert(0, str(MODULE_DIR))

import grainlearning as GL

grainlearning_config = {
    "simulations": {
        "num_samples": 14,
        "parameters": {"names": ["M", "C"], "mins": [3, 3], "maxs": [7, 7]},
    },
    "observations": {
        "data": [[5, 10, 15, 20 ]],
        "control": [0, 1, 2, 3],
    },
    "calibration": {
        "inference": { "ess_target": 0.9, "inv_obs_weight": [1]},
        "sampling": {"max_num_components": 1},
    },
}


sample_list = []
M = []
C = []

class linear_model(GL.Simulations):
    num_samples = 10
    
    parameters = GL.Parameters()

    def run(self):
        global sample_list,parameters_list
        params = self.get_params()
        control = self.observations.control
        self.state = []
        M_collect = []
        C_collect = []
        for i in range(self.num_samples):

            sample_result = [
                self.f_lin(x, params[i]["M"], params[i]["C"]) for x in control
            ]
            M_collect.append(params[i]["M"])
            C_collect.append(params[i]["C"])
            self.state.append([sample_result])
        self.state = np.array(self.state)
        M.append(M_collect)
        C.append(C_collect)
        sample_list.append(self.state)
        print(self.state.shape)


gl_toolbox = GL.CalibrationToolbox.from_dict(grainlearning_config, linear_model)

gl_toolbox.run()

#%%
import matplotlib.pyplot as plt

sample_list = np.array(sample_list)
plt.plot( [5, 10, 15,20 ],c='black',ls='-',marker='x',label ="Analytical")
for i in range(14):
    plt.plot(sample_list[3][i][0],c='grey',ls='--',alpha=0.2)
    plt.plot(sample_list[4][i][0],c='b',ls='--',alpha=0.3)
    # plt.plot(sample_list[5][i][0],c='g',ls='--',alpha=0.4)
    # plt.plot(sample_list[6][i][0],c='red',ls='--',alpha=0.5)

plt.legend()

# %%

plt.plot(gl_toolbox.sigma_list)
#%%

sample_list[9][i][0]

# %%

# plt.scatter(M[0],C[0])

plt.plt.scatter(M[1],C[1])
# %%
