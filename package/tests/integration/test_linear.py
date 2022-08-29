
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd


# import os
# import sys
# from pathlib import Path

# import numpy as np



# PROJECT_DIR = BASE_DIR = Path(__file__).resolve().parent

# MODULE_DIR = PROJECT_DIR.parent.parent.parent

# sys.path.insert(0, str(MODULE_DIR))

# from pyroclastpy.GeometryGenerators import create_line,create_circle,create_sphere # helper function
# from pyroclastpy import Solver, ParticlesContainer, NodesContainer, LinearElastic, LinearShapeFunction, QuadraticShapeFunction, ostream_redirect


# steps = 100

# dstart,dend = [0,10]

# spread = 1.5

# c = 2

# m = 0.4

# f = lambda x: c*x + c

# x = np.linspace(dstart,dend,steps)

# y = f(x)

# noise = np.random.normal(0,spread,steps)

# y_observation = y +noise

# # %%

# plt.plot(x,y)
# plt.scatter(x,model_y,marker="x",c='r')

# # %%

# df = pd.DataFrame({"control":x,
#                    "observation":y_observation
#                    })
# # %%
# df.head()
# # %%
