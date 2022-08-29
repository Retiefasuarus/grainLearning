import numpy as np
from scipy.stats import qmc


def generate_halton(dim,num_samples,mins,maxs):
    halton_sampler = qmc.Halton(d=dim, scramble=False)
    table = halton_sampler.random(n=num_samples)
    
    for i in range(dim):
        for j in range(num_samples):
            mean = .5 * (maxs[i] + mins[i])
            std = .5 * (maxs[i] - mins[i])
            table[j][i] = mean + (table[j][i] - .5) * 2 * std
    
    return table