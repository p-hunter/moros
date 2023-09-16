import numpy as np
import scipy.stats as stats


def Mode(x):
  k = stats.gaussian_kde(x)
  h = k.pdf(x)
  return(x[np.argmax(h)])
