
"""
Description:
This script takes in 2 or 3 arguments and uses them to print either a song or movie description.
It uses strip() to get rid of trailing and leading spaces.

Example output:
python3 A9E1.py '     extraction 2   ' '   sam harGRAVE  ' '   Chris hemsworth  '

The movie sequel is "Extraction 2", directed by Sam Hargrave, starring Chris Hemsworth
"""

from sys import argv

# Prints out description depending on if there is a digit in the movie title
def get_movie_desc(title, director, actor):
    if any(char.isdigit() for char in title):
        return f"The movie sequel is \"{title.title()}\", directed by {director.title()}, starring {actor.title()}"
    else:
        return f"The movie is \"{title.title()}\", directed by {director.title()}, starring {actor.title()}"

# Prints the song description
def get_song_desc(title, artist):
    return f"The song is {title.upper()} by {artist.title()}"

# Strips all the arguments to make sure there are no leading or trailing spaces
def clean_string(string):
    string = string.strip()
    words = string.split()
    return ' '.join(words)

def main():
    args = len(argv) - 1
    print(f"{args} args and {*argv,}")
    if args == 2:
        result = get_song_desc(clean_string(argv[1]), clean_string(argv[2]))
        print(result)
    elif args == 3:
        result = get_movie_desc(clean_string(argv[1]), clean_string(argv[2]), clean_string(argv[3]))
        print(result)
    elif args == 1:
        print("Error: Missing parameters")

if __name__ == "__main__":
    main()