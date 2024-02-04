import numpy as np
np.array([1,2,3])
np.array([[1,2,3],[2,4,6]]) #2d array
np.array([[[1,2,3],[2,4,6]],[[4,6,8],[9,11,13]]]) #three dimensional array

arr = np.zeros((4,4)) #array contains zero with float dtype

matrix = np.zeros((3,3),dtype=int)
np.ones((2,3))
arr = np.full((2,3),fill_value=100)
arr = np.empty((3,3))
np.eye(5,dtype=int) #diagonal elements are set to zero others 1
print(arr)
