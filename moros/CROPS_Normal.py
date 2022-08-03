
import numpy as np

def CROPS_Normal(x):
    
    mu = np.mean(x)
    x_dmu = x - mu
    x = np.insert(x, 0, 0)
    x_dmu = np.insert(x_dmu, 0,0)
    xx = x
    xx_s = np.cumsum(xx)
    xx_ss = np.cumsum(xx**2)
    x_dmu_ss = np.cumsum(x_dmu ** 2)
    sum_stat = np.array([xx_s, xx_ss, x_dmu_ss] )
    
    
    
    return(penalty_range(sum_stat))
