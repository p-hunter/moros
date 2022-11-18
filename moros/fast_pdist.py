




def fast_pdist(x):
  
  """
  Just a bad attempt at a very fast pair-wise Euclidian distance matrix
  
  Needs testing extensively!
  
  Was sick of iterating
  
  """
  
  import numpy as np
  
  xn = map(np.dot, [x.T,x])
  
  n = len(x)
  
  m_temp = [xn] * n
  
  m_temp = xn + [xn.T] * n
  
  return(sqrt(m_temp - 2 * np.dot(x, x.T)))
  
  
  
  
  
