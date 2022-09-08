import numpy as np

a = np.array([[2, 3], [5, 2]])
print(a)
d = np.array([2, 3, 4, 5, 6])

print(d)
print(d.shape)
e = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
print(e.shape)
print(e.dtype)
print(np.zeros((2, 10)))
print(np.ones((2, 10)))
print(np.arange(2, 10))


a = np.ones((2, 3))
print(a)
b = np.transpose(a)
print(b)

arr1 = np.array([[2, 3, 4], [6, 7, 8]])
arr2 = np.array([[12, 13, 14], [16, 17, 18]])

print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)

d = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6, 7], [5, 6, 4, 7, 8, 9, 9]])
d_list = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6, 7], [5, 6, 4, 7, 8, 9, 9]]
print(d_list)
print(type(d_list))
# d_list[:2] = 0 ==> error
d_list[2] = 0
print(d_list)
print('---------------------')
print(d)
d[:2] = 0
print(d)
print(np.arange(10))
arr4 = np.arange(10)+1
print(arr4)
print(arr4[:5])
print(arr4[-3:])
print(arr1)
print(arr1[1, 2])
print(arr1[:, 2])
