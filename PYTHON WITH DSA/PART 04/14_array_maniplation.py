import numpy as np 
a = np.arange(1,5)
# print(a)
b = np.arange(11,15)
# print(b)

# # copy to 
# np.copyto(a,b)

# # shape
# print(np.shape(a))

# # ndim 
# print(np.ndim(a))

# # size 
# print(np.size(a))

# reshape
# c = np.reshape(a,(2,2))
# c = np.reshape(a,(2,2),order="F")
# # c = np.reshape(a,(2,2),order="A")
# # c = np.reshape(a,(2,2),order="C")
# print(c)

# resize
# print(np.resize(a,(6,6)),np.shape)

# flatten 
# A = np.array([[[1,2,3,4,5],[5,6,7,8,9]],[[1,2,3,4,5],[7,8,9,6,5]]])
# print(A.flatten("F"))

#  reval 
# A = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[1,2,3,4,5],[6,7,8,9,10]]])
# print(np.ravel(A))
# print(np.ravel(A,order="F"))
# print(np.ravel(A,order="C"))
# print(np.ravel(A,order="A"))


#transpose 
# A = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[7,8,9],[10,11,12],[13,14,15]]])
# print(A,A.shape,A.ndim)
# print(np.transpose(A),np.shape(A))
# a = A.transpose()
# print(a)
# print(np.transpose(A,(0,1)))

# swapaxes
# a=np.arange(1,11).reshape(2,5)
# a = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[7,8,9],[10,11,12],[13,14,15]]])

# print(a,a.shape,a.ndim)
# print(np.swapaxes(a,0,2))
# print(np.swapaxes(a,2,0))


# spiting 
a = np.array([1,2,3,4,5,6,7,8,9])
print(a)
print()
