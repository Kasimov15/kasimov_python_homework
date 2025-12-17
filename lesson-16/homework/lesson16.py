# ==================================================
# NUMPY HOMEWORK 
# ==================================================

import numpy as np

# --------------------------------------------------
# 1. Convert List to 1D Array
# --------------------------------------------------
lst = [12.23, 13.32, 100, 36.32]
arr1 = np.array(lst)
print("1) Original List:", lst)
print("   One-dimensional NumPy array:", arr1)
print()

# --------------------------------------------------
# 2. Create 3x3 Matrix (2 to 10)
# --------------------------------------------------
matrix = np.arange(2, 11).reshape(3, 3)
print("2) 3x3 Matrix from 2 to 10:")
print(matrix)
print()

# --------------------------------------------------
# 3. Null Vector (10) & Update Sixth Value
# --------------------------------------------------
null_vec = np.zeros(10)
print("3) Null vector:")
print(null_vec)

null_vec[6] = 11
print("   Update sixth value to 11:")
print(null_vec)
print()

# --------------------------------------------------
# 4. Array from 12 to 38
# --------------------------------------------------
arr_range = np.arange(12, 38)
print("4) Array from 12 to 38:")
print(arr_range)
print()

# --------------------------------------------------
# 5. Convert Array to Float Type
# --------------------------------------------------
arr_int = np.array([1, 2, 3, 4])
arr_float = arr_int.astype(float)
print("5) Original array:", arr_int)
print("   Float array:", arr_float)
print()

# --------------------------------------------------
# 6. Celsius to Fahrenheit Conversion
# --------------------------------------------------
celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = (celsius * 9 / 5) + 32

print("6) Values in Centigrade degrees:", celsius)
print("   Values in Fahrenheit degrees:", fahrenheit)
print()

# --------------------------------------------------
# 7. Append Values to Array
# --------------------------------------------------
arr = np.array([10, 20, 30])
new_arr = np.append(arr, [40, 50, 60, 70, 80, 90])

print("7) Original array:", arr)
print("   After append values:", new_arr)
print()

# --------------------------------------------------
# 8. Array Statistical Functions
# --------------------------------------------------
random_arr = np.random.rand(10)
print("8) Random array:", random_arr)
print("   Mean:", np.mean(random_arr))
print("   Median:", np.median(random_arr))
print("   Standard Deviation:", np.std(random_arr))
print()

# --------------------------------------------------
# 9. Find Min and Max (10x10 array)
# --------------------------------------------------
arr_10x10 = np.random.rand(10, 10)
print("9) 10x10 Random Array:")
print(arr_10x10)
print("   Minimum value:", arr_10x10.min())
print("   Maximum value:", arr_10x10.max())
print()

# --------------------------------------------------
# 10. Create 3x3x3 Array with Random Values
# --------------------------------------------------
arr_3d = np.random.rand(3, 3, 3)
print("10) 3x3x3 Random Array:")
print(arr_3d)
