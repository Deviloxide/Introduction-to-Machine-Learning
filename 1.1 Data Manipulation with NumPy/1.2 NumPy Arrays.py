import numpy as np

arr = np.array([np.nan, 2, 3, 4, 5])

arr2 = arr.copy()
arr2[0] = 10

float_arr = np.array([1, 5.4, 3])
float_arr2 = arr2.astype(dtype=np.float32)

matrix = np.array([[1,2,3],[4,5,6]], dtype=np.float32)
