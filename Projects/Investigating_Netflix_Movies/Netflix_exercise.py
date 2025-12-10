
import pandas as pd
import matplotlib.pyplot as plt


# Reading the CSV file
netflix =  pd.read_csv('../../Data/netflix_data.csv')

# Most frequent movie duration in the 1990s
movies = netflix.loc[netflix['type'] == 'Movie']
r90s = movies.loc[movies['release_year'] >= 1990]
movies_90s = r90s.loc[r90s['release_year'] < 2000]
print(len(movies_90s))

# Create an histogram to identify 
plt.hist(movies_90s["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

# Filter the data again to keep only the Action movies
action = movies_90s[movies_90s["genre"] == "Action"]


# Start the counter
short_movie_count = 0

# Iterate over the labels 
for label, row in action.iterrows() :
    if row["duration"] < 90 :
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count

print(short_movie_count)