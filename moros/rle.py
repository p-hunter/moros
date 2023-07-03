import numpy as np

def rle(x):
  
  """ this is run-length encoding for Boolean and Integer values. 
  This can be adopted for peak-detection for time-series data.
  Thats p much why it exists, no other real reason"""
  
  N = len(x)
  
  print("Length: {}".format(N))
  
  if N == 0:
    return dict({"lengths": [0], "values":x})

  y = np.array(x[1:]) != np.array(x[:-1])
 
  i = np.where(y)[0]
  
  i = (np.append(i, N-1) )

  x = [x[j] for j in i] 
  
  Di = np.diff(np.append(0, i))
  
  Di[0] = Di[0] + 1
  
  return list(Di), x

# TEST EXAMPLES
#
# should be lengths 3, 2, 1, 2, 4 for values 1, 2, 3, 2, 1
# test1 = [1, 1, 1, 2, 2, 3, 2, 2, 1, 1, 1, 1] 
# 
# print(rle(test1))
# 
# should be lenths: 2, 3, 4, 1 for values True, False, True, False 
# test2 = [True, True, False, False, False, True, True, True, True, False] 
# 
# print(rle(test2))
#

