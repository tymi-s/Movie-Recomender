def return_all_genres(movies):
    ganres = set()
    for movie in movies:
        ganres.update(movie['genre'])

    return ganres