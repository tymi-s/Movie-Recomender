from return_all_genres import *
from change_movie_status import *
from display_recomended import *
from display_by_genre import *
from find_watched_movies import *
movies = [
    {"title": "Inception", "genre": {"Sci-Fi", "Thriller"}, "rating": 8.5, "year": 2010, "status": "not watched"},
    {"title": "Interstellar", "genre": {"Sci-Fi", "Adventure"}, "rating": 10.0, "year": 2014, "status": "not watched"},
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
print(f"\n\n{"="*50 } WELCOME TO MOVIES RECOMENDER APP!!! {"="*50}")

while True:
    print(f"\n\n{"="*50 } MAIN MENU {"="*50}\n\n")
    print("1 - Display all movies\n2 - Change a status of a movie\n3 - Display recomended movies\n4 - Display movies by ganre\n5 - Display all genres\n6 - Display watched movies\n7 - Exit")
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            print(f"{"="*50 } LIST OF ALL MOVIES: {"="*50}\n")
            for movie in movies:
                print(movie)

        case "2":
            print(f"{"="*50 } CHANGING MOVIE STATUS: {"="*50}\n")
            while(True):

                movie_name = input("Enter movie's name: ")
                ret, watched_genres =change_movie_status(movie_name, movies)
                if ret == True:
                    print("\nMovie's status changed successfully!")
                    break
        case "3":
            print(f"{"=" *50} DISPLAYING RECOMENDED MOVIES: {"=" *50}\n")
            recomended = display_recomended_movies(watched_genres,movies)
            for movie in recomended:
                print(movie)


        case "4":
            print(f"{"=" * 50} DISPLAYING MOVIES BY GENRE: {"=" * 50}\n")
            for genre in ganres:
                display_by_genre(genre,movies)


        case "5":
            print(f"{"=" * 50} DISPLAYING ALL GENRES: {"=" * 50}\n")
            print(ganres)
        case "6":
            find_watched_movies(movies)
            pass
        case "7":
            print("SEE YOU LATER ALIGATOR! ;*")
            break
        case _:
            print("\nThere is no such option in menu! Try again! ;)")









