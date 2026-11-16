#!/usr/bin/env python3
# Author: Marky
# Date: November 16, 2026
# Purpose: Create Histograms.
# Usage: ./lab7h.py

# TO DO 1: Import pandas and matplotlib modules
import pandas as pd
import matplotlib.pyplot as plt

# TO DO 2: Read the movies database
df = pd.read_csv("imdb_top_250.csv")

# TO DO 3: Perform the required operations

# Copy the Year column into a new series
years = df["Year"].dropna()

# Sort years in ascending order
years = years.sort_values()

print("Sorted Years:")
print(years)

# Find unique years and count how many times each year occurs
year_counts = years.value_counts().sort_index()

print("\nUnique Years and Number of Movies:")
print(year_counts)

# Display only the first 10 years if there are many unique years
if len(year_counts) > 10:
    year_counts = year_counts.head(10)

# Draw histogram using a bar chart
plt.bar(year_counts.index, year_counts.values)

plt.title("Number of Movies Released Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Movies")

plt.show()

# TO DO 4: Run the script