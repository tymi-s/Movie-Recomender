def display_by_genre(genre,movies):

    g=genre.upper()
    print(f"\n{g} MOVIES:\n\n")
    for movie in movies:
        if genre in movie['genre']:
            print(f"{movie}")
