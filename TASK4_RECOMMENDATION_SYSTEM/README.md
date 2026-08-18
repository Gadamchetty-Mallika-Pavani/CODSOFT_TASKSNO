# Movie Recommendation System

## Project Description

This project is a simple movie recommendation system developed using Python as part of my CodSoft Artificial Intelligence Internship.

The system recommends movies based on the similarity between their genres and descriptions. It uses a content-based filtering approach to find movies that are similar to the movie selected by the user.

## Features

- Displays a list of available movies
- Accepts a movie name from the user
- Finds similar movies
- Provides up to 5 recommendations
- Uses content-based filtering
- Uses TF-IDF vectorization
- Uses cosine similarity to calculate movie similarity

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

## How It Works

The system follows these steps:

1. Loads movie information from `movies.csv`.
2. Combines the genre and description of each movie.
3. Converts the text data into numerical vectors using TF-IDF.
4. Calculates similarity between movies using cosine similarity.
5. Finds the movies most similar to the user's selected movie.
6. Displays the top recommendations.

## How to Run

Install the required libraries:

```bash
pip install pandas scikit-learn