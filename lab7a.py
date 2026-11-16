#!/usr/bin/env python3
# Author: Marky
# Date: November 13, 2026
# Purpose: Create Arrays.
# Usage: ./lab7a.py

# Import NumPy
import numpy as np

# TO DO 1: Create array1 and array2 using two different methods
array1 = np.arange(20, 50)
array2 = np.array(list(range(20, 50)))

# Display array1 and array2
print("Array 1:", array1)
print("Array 2:", array2)

# TO DO 2: Create a 3x3 matrix with values from 1 to 9
array3 = np.arange(1, 10).reshape(3, 3)

# Display array3
print("\nArray 3:")
print(array3)

# TO DO 3: Create a 3D matrix of shape 2x3x2 with month names
array4 = np.array([
    [["January", "February"],
     ["March", "April"],
     ["May", "June"]],

    [["July", "August"],
     ["September", "October"],
     ["November", "December"]]
])

# Display array4
print("\nArray 4:")
print(array4)