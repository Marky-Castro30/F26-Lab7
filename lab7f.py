#!/usr/bin/env python3
# Author: Marky
# Date: November 16, 2026
# Purpose: Create Data Frames.
# Usage: ./lab7f.py

# Import pandas module
import pandas as pd

# TO DO 1: Create dataframe from provided dictionaries

# Create the dictionaries
colors = {
    "Apple": "Green",
    "Carrot": "Red",
    "Radish": "Purple"
}

shapes = {
    "Okra": "Thin",
    "Potato": "blob",
    "Radish": "Round"
}

prices = {
    "Apple": 2.1,
    "Okra": 3.5,
    "Carrot": 1.3,
    "Potato": 2.0,
    "Radish": 3.0
}

# Combine the dictionaries into one DataFrame
df = pd.DataFrame({
    "Color": colors,
    "Shape": shapes,
    "Price": prices
})

# Display the DataFrame
print("DataFrame from dictionaries:")
print(df)


# TO DO 2: Create a DataFrame from dataframe.jpg

data = {
    "student name": ["A", "B", "C", "D"],
    "student marks": [22, 344, 55, 77]
}

df2 = pd.DataFrame(data, index=["Maths", "English", "Urdu", "Science"])

print("\nStudent DataFrame:")
print(df2)

# TO DO 3: Run the script