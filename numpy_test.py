import numpy as np
print(np.__version__)
my_list = [1, 2, 3,4]
print(my_list * 2, "python array")
print(np.array(my_list) * 2, "numpy array")

array = np.array("A")
print(array.ndim, "number of dimensions of the array ['a']")
print(array.shape, "shape of the array ['a']")

array = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [10, 11, 12]]])
print(array[0,0,0], "first element of the array")

num =str(array[0,1,2]) + " " +str(array[1,0,0])
print(num, "six and seven")

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])
#array[start:end:step]
print(array[::-2,0], "slicing the array")