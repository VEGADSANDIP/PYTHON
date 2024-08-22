import numpy as np

a = np.array([12,3,4,5,6,7,8])
print(a,type(a),a.ndim)


a = np.array([[1,2,3],[4,5,6]])
print(a,type(a))

a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a,type(a),a.ndim)

a = np.array([[1,2,3],[4,5,6]],"complex")
print(a,type(a))

