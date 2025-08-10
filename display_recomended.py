def display_recomended_movies(movie_genre,movies):
    to_display = []
    for movie in movies:
        for genres in movie['genre']:
            if genres in movie_genre:
                to_display.append(movie) if movie['status'] == 'not watched' else None

    return to_display
