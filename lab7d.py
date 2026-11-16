#!/usr/bin/env python3
# Author: Marky
# Date: November 13, 2026
# Purpose: Slicing 2D NumPy Arrays.
# Usage: ./lab7d.py

# Import NumPy
import numpy as np

# TO DO 1: Create the given 2D NumPy array
arr_2d = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [110, 120, 130, 140, 150],
    [160, 170, 180, 190, 200]
])

print("Original Array:")
print(arr_2d)

# TO DO 2: Perform slicing operations

# Slice the first two rows and last three columns
slice_1 = arr_2d[:2, -3:]

print("\nSlice 1:")
print(slice_1)

# Extract the middle 2x2 subarray
slice_2 = arr_2d[1:3, 1:3]

print("\nSlice 2:")
print(slice_2)

# Slice every other row and every other column
slice_3 = arr_2d[::2, ::2]

print("\nSlice 3:")
print(slice_3)