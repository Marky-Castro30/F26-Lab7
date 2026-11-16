#!/usr/bin/env python3
# Author: Marky
# Date: November 13, 2026
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py

import numpy as np

# TO DO 1: Create numArray with 100 random numbers
numArray = np.random.randint(1, 101, 100)

print("Original Array:")
print(numArray)

# TO DO 2: Perform slicing operations

# Slice and print the first 10 values
print("\nFirst 10 values:")
print(numArray[:10])

# Slice and print the last 10 values
print("\nLast 10 values:")
print(numArray[-10:])

# Slice and print 30 values starting from index 21
print("\n30 values starting from index 21:")
print(numArray[21:51])

# Change all values from index 50 to 65 to 101
numArray[50:66] = 101

print("\nUpdated Array:")
print(numArray)

# TO DO 3: Run the script