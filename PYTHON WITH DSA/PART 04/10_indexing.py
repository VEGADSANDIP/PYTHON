import numpy as np

arr = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
print(arr,arr.ndim,arr.shape)
print(arr[1][1])


import numpy as np

arr = np.arange(0,10)
index = np.array([2,6,7])
print(arr[index])

arr = np.array([[1,54,6],[6,2,4]])
index = np.array([[0,1],[1,0]])
print(arr[index])