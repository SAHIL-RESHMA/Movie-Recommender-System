"""
Movie Recommender System (User-Based Collaborative Filtering)

This script builds a user-based collaborative filtering recommender system
using the MovieLens 100k dataset. It analyzes user ratings and suggests
movies similar to a given target movie using Pearson correlation.
"""

# ==============================================================================
# 📦 Import Required Libraries
# ==============================================================================
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set default style for plots
sns.set_style("white")

# ==============================================================================
# 📥 Load and Merge Dataset
# ==============================================================================

# File paths
RATINGS_PATH = "data/u.data"
MOVIES_PATH = "data/Movie_Id_Titles"

# Define column names for ratings data
rating_columns = ["user_id", "item_id", "rating", "timestamp"]

# Load user ratings data
ratings_data = pd.read_csv(RATINGS_PATH, sep="\t", names=rating_columns)

# Load movie title mappings
movie_titles = pd.read_csv(MOVIES_PATH)

# Merge ratings and titles on 'item_id'
df = pd.merge(ratings_data, movie_titles, on="item_id")

# ==============================================================================
# 📊 Ratings Analysis
# ==============================================================================

# Compute average rating and number of ratings per movie
movie_stats = df.groupby("title")["rating"].agg(["mean", "count"])
movie_stats.rename(columns={"mean": "average_rating", "count": "num_of_ratings"}, inplace=True)

# Create user-item rating matrix
user_movie_matrix = df.pivot_table(index="user_id", columns="title", values="rating")

# ==============================================================================
# 🎯 Find Similar Movies Function
# ==============================================================================

def get_similar_movies(target_movie: str, min_ratings: int = 100) -> pd.DataFrame:
    """
    Returns movies similar to the given target movie based on user rating patterns.

    Parameters:
        target_movie (str): Movie title to find similarities for.
        min_ratings (int): Minimum number of ratings required to consider a movie.

    Returns:
        pd.DataFrame: Sorted DataFrame of similar movies with correlation and rating count.
    """
    if target_movie not in user_movie_matrix.columns:
        raise ValueError(f"Movie '{target_movie}' not found in the dataset.")

    # Get ratings for the target movie
    target_ratings = user_movie_matrix[target_movie]

    # Compute Pearson correlation between target movie and all others
    correlations = user_movie_matrix.corrwith(target_ratings)
    corr_df = pd.DataFrame(correlations, columns=["correlation"])
    corr_df.dropna(inplace=True)

    # Join with number of ratings
    corr_df = corr_df.join(movie_stats["num_of_ratings"])

    # Filter by minimum number of ratings
    recommendations = corr_df[corr_df["num_of_ratings"] > min_ratings]
    recommendations = recommendations.sort_values("correlation", ascending=False)

    return recommendations

# ==============================================================================
# 📌 Example Usage
# ==============================================================================

if __name__ == "__main__":
    try:
        movie_to_search = "Star Wars (1977)"
        print(f"\nTop Recommendations Similar to '{movie_to_search}':\n")

        top_recommendations = get_similar_movies(movie_to_search, min_ratings=100)
        print(top_recommendations.head(10))  # Show top 10

    except ValueError as err:
        print(f"Error: {err}")
