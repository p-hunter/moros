import numpy as np
from scipy.optimize import brentq
import matplotlib.pyplot as plt

# learn more about u-quadratic distribution here: 
# https://www.irjmets.com/uploadedfiles/paper//issue_3_march_2024/50124/final/fin_irjmets1709731390.pdf

def uquad_cdf_inv(x: float, u: float, a: int,  alpha: float, beta: float) -> float:  
  return (x ** 3) - (3 * beta * (x ** 2 )) + (3 *  (beta ** 2) * x ) -  (((3 * u) / alpha) - ((beta - a) ** 3) + (beta ** 3)) 

def ruquad(n: int, a: int, b: int) -> list:  
  alpha = 12 / ((b - a)**3)
  beta = (a + b)/2  
  u = np.random.uniform(0, 1, n)
  # the min and max (2nd and 3rd arg) needs changing for values of b > 100 obvs
  res = [brentq(uquad_cdf_inv, -a, b, args=(u[i], a, alpha, beta)) for i in range(len(u))]   
  return res
