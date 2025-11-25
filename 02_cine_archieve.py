import os
import json

# Name of the JSON file that stores all movie data
FILENAME = "movies.json"


def load_movies():
    """
    Load the list of movies from the JSON file.
    If the file doesn't exist yet, return an empty list.
    """
    if not os.path.exists(FILENAME):
        print("No Movies File Found.")
        return []

    # Open and read the JSON file, then return the parsed list
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)


def save_movie(movie):
    """
    Save the entire list of movies back to the JSON file.
    This overwrites the existing file with the updated list.
    """
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(movie, f, indent=2)
        print("Movie Added Successfully. ✅")


def add_movie(movies):
    """
    Prompt the user for a new movie's details and add it to the list.
    Checks for duplicate titles and validates the rating.
    """
    title = input("Enter Movie Title: ").strip()

    # Prevent duplicate titles (case-insensitive check)
    if any(movie["title"].lower() == title.lower() for movie in movies):
        print("Movie with this title already exists.")
        return

    genre = input("Enter Movie Genre: ").strip()

    # Validate rating: must be a number between 0 and 10
    try:
        rating = float(input("Enter Movie Rating (0-10): ").strip())
        if not (0 <= rating <= 10):
            raise ValueError
    except ValueError:
        print("Invalid Rating. Please enter a number between 0-10.")
        return

    # Create new movie dictionary and append to the list
    new_movie = {"title": title, "genre": genre, "rating": rating}
    movies.append(new_movie)
    save_movie(movies)


def view_movies(movies):
    """
    Display all movies in a formatted list.
    Shows a friendly message if no movies exist.
    """
    if not movies:
        print("No Movies Found.")
        return
    print("-" * 40)
    print("🍿 Movie Database 🍿")
    for movie in movies:
        print(f"🎬 {movie['title']} | 🎭 {movie['genre']} | ⭐ {movie['rating']}")
    print("-" * 40)


def search_movie(movies):
    """
    Search for movies by title or genre (partial, case-insensitive match).
    Displays matching results using the same format as view_movies.
    """
    search_term = input("Enter Title or Genre to Search: ").strip()

    # Collect movies whose title or genre contains the search term
    results = [
        movie
        for movie in movies
        if search_term.lower() in movie["title"].lower()
        or search_term.lower() in movie["genre"].lower()
    ]

    if not results:
        print("No Movies Found.")
        return
    view_movies(results)


def run_movie_db():
    """
    Main interactive loop for the movie database program.
    Presents a menu and handles user choices.
    """
    # Load existing movies at startup
    movies = load_movies()

    print("Welcome to the Movie Database!")
    while True:
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie by Title or Genre")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        match choice:
            case "1":
                add_movie(movies)
            case "2":
                view_movies(movies)
            case "3":
                search_movie(movies)
            case "4":
                print("Exiting Movie Database. Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1-4.")


# Run the program only when this script is executed directly
if __name__ == "__main__":
    run_movie_db()
