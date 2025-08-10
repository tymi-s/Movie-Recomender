from return_all_genres import *
from change_movie_status import *
from display_recomended import *
movies = [
    {"title": "Inception", "genre": {"Sci-Fi", "Thriller"}, "rating": 8.5, "year": 2010, "status": "not watched"},
    {"title": "Interstellar", "genre": {"Sci-Fi", "Adventure"}, "rating": 10.0, "year": 2014, "status": "not watched"},
    {"title": "Interstellar", "genre": {"Sci-Fi", "Drama"}, "rating": 8.6, "year": 2014, "status": "not watched"},
    {"title": "The Dark Knight", "genre": {"Action", "Crime", "Drama"}, "rating": 9.0, "year": 2008, "status": "not watched"},
    {"title": "The Matrix", "genre": {"Sci-Fi", "Action"}, "rating": 8.7, "year": 1999, "status": "not watched"},
    {"title": "The Godfather", "genre": {"Crime", "Drama"}, "rating": 9.2, "year": 1972, "status": "not watched"},
    {"title": "Pulp Fiction", "genre": {"Crime", "Drama"}, "rating": 8.9, "year": 1994, "status": "not watched"},
    {"title": "Parasite", "genre": {"Thriller", "Drama"}, "rating": 8.6, "year": 2019, "status": "not watched"},
    {"title": "Avengers: Endgame", "genre": {"Action", "Adventure", "Sci-Fi"}, "rating": 8.4, "year": 2019, "status": "not watched"},
    {"title": "Toy Story", "genre": {"Animation", "Comedy", "Adventure"}, "rating": 8.3, "year": 1995, "status": "not watched"},
    {"title": "The Shawshank Redemption", "genre": {"Drama"}, "rating": 9.3, "year": 1994, "status": "not watched"},
    {"title": "Whiplash", "genre": {"Drama", "Music"}, "rating": 8.5, "year": 2014, "status": "not watched"},
    {"title": "Gladiator", "genre": {"Action", "Drama"}, "rating": 8.5, "year": 2000, "status": "not watched"},
    {"title": "Coco", "genre": {"Animation", "Adventure", "Family"}, "rating": 8.4, "year": 2017, "status": "not watched"},
    {"title": "Get Out", "genre": {"Horror", "Thriller"}, "rating": 7.7, "year": 2017, "status": "not watched"},
    {"title": "Mad Max: Fury Road", "genre": {"Action", "Adventure", "Sci-Fi"}, "rating": 8.1, "year": 2015, "status": "not watched"}
]

watched_genres = set()
ganres= return_all_genres(movies)
print(f"\n\n{"="*25 } WELCOME TO MOVIES RECOMENDER APP!!! {"="*25}")

while True:
    print("\n\n1 - Display all movies\n2 - Change a status of a movie\n3 - Display recomended movies\n4 - Display movies by ganre\n5 - Display all genres\n6 - Exit")
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            print(f"{"="*25 } LIST OF ALL MOVIES:\n {"="*25}")
            for movie in movies:
                print(movie)

        case "2":
            print(f"{"="*25 } CHANGING MOVIE STATUS: {"="*25}\n")
            while(True):

                movie_name = input("Enter movie's name: ")
                ret, watched_genres =change_movie_status(movie_name, movies)
                if ret == True:
                    break
        case "3":
            print(f"{"=" * 25} DISPLAYING RECOMENDED MOVIES: {"=" * 25}\n")
            recomended = display_recomended_movies(watched_genres,movies)
            print(recomended)


        case "4":
            pass

        case "5":
            print(ganres)
        case "6":
            break










