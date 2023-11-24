import sys

def main():
    args = sys.argv[1:]
    cleaned_args = [clean_string(arg) for arg in args]

    if len(cleaned_args) == 2:
        print(get_song_desc(*cleaned_args))
    elif len(cleaned_args) >= 3:
        print(get_movie_desc(*cleaned_args))
    else:
        print("Error: Missing parameters")

def clean_string(s):
    return ' '.join(s.strip().split())

def get_song_desc(title, artist):
    return f"The song is {title.upper()} by {artist.title()}"

def get_movie_desc(title, director, actor):
    if any(char.isdigit() for char in title):
        desc = "The movie sequel is"
    else:
        desc = "The movie is"
    return f'{desc} "{title.title()}", directed by {director.title()}, starring {actor.title()}'

if __name__ == "__main__":
    main()
