import scipy as sp
import numpy as np

def neg_loglik(x):
    return(-np.log(sp.stats.norm.pdf(x)).sum())
