
def change_movie_status(movie_name,movies):
    watched = set()
    for movie in movies:
        if movie['title'] == movie_name:
            movie['status'] = 'watched'
            watched.update(movie['genre'])
            return True, watched
    print("No movie witch such was found on a list! Try again later!")
    return False, watched