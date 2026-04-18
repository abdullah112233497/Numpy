import numpy as np

arr1=np.array(
    [[1,2,3],
    [4,5,6]

])
array1=np.array([43,53,23,12])
array2=np.array([6,7,8,2])


# print("dimension: ",np.concatenate((array1,array2)))
# print(array1.shape)
# # Ouput: (4,)
# print("Equal: ", array1.shape==array2.shape)


# Vectorized
vvv=np.array(["abullah","ali"])
vector=np.vectorize(str.upper)
print("Vectorized operation: ",vector(vvv))
