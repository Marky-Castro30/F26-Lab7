#!/usr/bin/env python3
# Author: Marky
# Date: November 13, 2026
# Purpose: Create Series.
# Usage: ./lab7e.py

# TO DO 1: Import pandas module
import pandas as pd

# TO DO 2: Create a series with grade ranges and index names
grades = pd.Series(
    ["<50", "50-59", "60-69", "70-79", "80-89", "90-100"],
    index=["F", "D", "C", "B", "A", "A+"]
)

# Display the series
print("Grade Series:")
print(grades)

# TO DO 3: Perform operations on the series

# Print the values of indices C and A+
print("\nValues of C and A+:")
print(grades[["C", "A+"]])

# Print value 60-69 without its index name
print("\nValue of C:")
print(grades["C"])

# Show the multiplication operation on the series
print("\nSeries multiplied by 2:")
print(grades * 2)

# TO DO 4: Run the script