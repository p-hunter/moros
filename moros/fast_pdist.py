def fast_pdist(x):
  
  """
  Just a bad attempt at a very fast pair-wise Euclidian distance matrix
  
  Needs testing extensively!
  
  Was sick of iterating
  
  """
  
  import numpy as np
  
  n = len(x)
  
  xn = [np.matmul(x[i].T, x[i]) for i in range(n)]
  
  m_temp_1= np.array([np.array(xn)] * n).T
  
  m_temp_2 =  m_temp_1.T
  
  m_temp = m_temp_1 + m_temp_2
  
  m_out = m_temp - 2 * np.matmul(x, x.T)
  
  return(sqrt(m_out))





