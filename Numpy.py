import numpy as np

# Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr_1d)

# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(arr_2d)

# Arithmetic operations
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Element-wise addition
result_add = arr1 + arr2
print("Element-wise Addition:")
print(result_add)

# Element-wise multiplication
result_mul = arr1 * arr2
print("\nElement-wise Multiplication:")
print(result_mul)

# Matrix multiplication
result_matmul = np.matmul(arr1, arr2)
print("\nMatrix Multiplication:")
print(result_matmul)

# Generating a random array
random_data = np.random.rand(3, 4)
print("Random Data:")
print(random_data)

# Calculating mean and standard deviation
mean_value = np.mean(random_data)
std_dev = np.std(random_data)

print("\nMean:", mean_value)
print("Standard Deviation:", std_dev)

# Reshaping a 1D array to a 2D array
arr_1d = np.arange(1, 10)
arr_2d = arr_1d.reshape(3, 3)
print("Original 1D Array:")
print(arr_1d)
print("\nReshaped 2D Array:")
print(arr_2d)

# Slicing an array
sliced_array = arr_2d[0:2, 1:3]
print("\nSliced Array:")
print(sliced_array)

#Slicing
# Creating a 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Accessing elements
element_00 = arr_2d[0, 0]
print("Element at [0, 0]:", element_00)

# Slicing
row_slice = arr_2d[1, :]
column_slice = arr_2d[:, 2]

print("\nRow Slice:")
print(row_slice)
print("Column Slice:")
print(column_slice)
