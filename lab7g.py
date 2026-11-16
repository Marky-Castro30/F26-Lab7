#!/usr/bin/env python3
# Author: Marky
# Date: November 16, 2026
# Purpose: Create data frame from CSV file.
# Usage: ./lab7g.py

# Import required modules
import pandas as pd
import matplotlib.pyplot as plt

# TO DO 1: Create a new data frame from the CSV file

url = "https://raw.githubusercontent.com/itiievskyi/IMDB-Top-250/master/imdb_top_250.csv"

df = pd.read_csv(url, index_col=0)

# Display the data frame
print("IMDb Movies DataFrame:")
print(df)


# TO DO 2: Perform the required operations

# 1. Print summary of the data
print("\nSummary of the Data:")
print(df.describe(include="all"))


# 2. Print first 10 and last 10 rows
print("\nFirst 10 Movies:")
print(df.head(10))

print("\nLast 10 Movies:")
print(df.tail(10))


# 3. Print earliest and latest movie year
print("\nEarliest Movie Year:")
print(df["Year"].min())

print("\nLatest Movie Year:")
print(df["Year"].max())


# 4. Print unique values in the Genre column
print("\nUnique Genres:")
print(df["Genre"].unique())


# 5. Count movies not made in the USA
not_usa = df[~df["Origin"].str.contains("USA", na=False)]

print("\nMovies not made in USA:")
print(len(not_usa))


# 6. Find the top 10 highest-rated movies
top_movies = df.sort_values(by="IMDB rating", ascending=False)

print("\nTop 10 Highest-Rated Movies:")
print(top_movies[["Title", "IMDB rating"]].head(10))


# 7. Find the best decade of movies

# Define a function to get the decade
def get_decade(year):
    return (year // 10) * 10


# Add a decade column
df["Decade"] = df["Year"].apply(get_decade)

# Group movies by decade and calculate average rating
decade_ratings = df.groupby("Decade")["IMDB rating"].mean()

print("\nAverage Movie Rating per Decade:")
print(decade_ratings)

# Find the best decade
best_decade = decade_ratings.idxmax()

print("\nBest Decade:")
print(best_decade)


# 8. Create a scatter plot
plt.scatter(decade_ratings.index, decade_ratings.values)

plt.title("Average IMDb Movie Rating per Decade")
plt.xlabel("Decade")
plt.ylabel("Average IMDb Rating")

plt.show()


# TO DO 3: Run the script