import numpy as np
import time
# timeStart=time.time()
# arr=np.array([1,2,4])
# print("Numpy Time: ", time.time()-timeStart)
# print (arr)
# timeStartSimple=time.time()

# arr_simple =[2,34,4]
# print("simple Time: ", time.time()-timeStartSimple)

# print (arr_simple)


arr_1d=np.array([1,23,22])
arr_2d=np.array([[1,2,3],[4,5,6]])
arr_tensor=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

arr=np.arange(10)
reshape=arr.reshape(5,2)
print("Size",reshape.size)
print("Dimension",reshape.ndim)



print(reshape)
print("Order",reshape.shape)
print("Transpose : ", reshape.T)
flatterned=reshape.flatten()
print("Order of flatten: ", flatterned.shape, flatterned)


