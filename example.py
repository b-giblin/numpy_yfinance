import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# print(arr[1:6])
# print(arr[1:6:2])
# print(arr[:6:2])
# print(arr[1::2])
# print(arr[::-1])


arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2[:2,:1])
print(arr2[:,2])
print(arr2[0:2, 1:3])


arr1 = np.array([[1, 2, 3, 4],[1, 2, 3, 4]])
print(arr1)

print(f"the shape of the array is: {arr1.shape}")
print(f"the size of the array is: {arr1.dtype}")
print(f"the size of the array is: {arr1.size}")


arr2 = np.array([[1, 2], [3, 4], [5, 6]])
print(f"the shape of the array is: {arr2.shape}")
print(f"the size of the array is: {arr2.size}")
print(f"the datatype of the array is: {arr2.dtype}")

arr3 = np.array([1, 2, 3, 4, 5])
arr4 = np.array([1, 2, 3, 4, 5])
print(arr3 + arr4)
print(arr3 * 2)

print(np.sqrt(arr3))
print(np.log(arr3))

arr5 = np.array([9, 16, 25, 36])
print(np.sqrt(arr5))


# Reshaping and Transposing
arr6 = np.array([[1,2,3], [4,5,6]])
print(arr6.reshape(3, 2))
print(arr6.T)


# Indexing and Slicing
print(arr1[1])
print(arr1[:, 1])

print('-' * 20)

# Linear Algebra with NumPy
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[2, 0], [0, 2]])
print(mat1, mat2)
print(np.dot(mat1, mat2))
print(mat1[0:2, 0])