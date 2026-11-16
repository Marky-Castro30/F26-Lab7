#!/usr/bin/env python3
# Author: Marky
# Date: November 13, 2026
# Purpose: Change Dimensions and create special arrays.
# Usage: ./lab7b.py

import numpy as np

# TO DO 1: Copy the code from lab7a.py

array1 = np.arange(20, 50)
array2 = np.array(list(range(20, 50)))

array3 = np.arange(1, 10).reshape(3, 3)

array4 = np.array([
    [["January", "February"],
     ["March", "April"],
     ["May", "June"]],

    [["July", "August"],
     ["September", "October"],
     ["November", "December"]]
])

# TO DO 2: Reshape array1 and array2

array1 = array1.reshape(5, 6)
array2 = array2.reshape(2, 3, 5)

print("Array 1 (5x6):")
print(array1)

print("\nArray 2 (2x3x5):")
print(array2)

# TO DO 3: Create array5 with diagonal values

array5 = np.diag([45, 7, 61, 8, 9])

print("\nArray 5 (5x5):")
print(array5)

# TO DO 4: Create array6 with random normal values

array6 = np.random.randn(7, 7)

print("\nArray 6 (7x7):")
print(array6)

# TO DO 5: Run the script