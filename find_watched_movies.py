def find_watched_movies(movies):
    watched_movies = []
    print(f"{"=" * 50} DISPLAYING WATCHED MOVIES {"=" * 50}\n")
    for movie in movies:
        if movie['status'] == "watched":
            watched_movies.append(movie)

    if(len(watched_movies) == 0):
        print( "\nNo movies are watched yet! :(")
        return 0
    else:

        for movie in watched_movies:
            print(movie)
        return watched_movies
