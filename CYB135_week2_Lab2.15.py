#CYB135 Week2 Lab 2.15
'''
2.15 LAB: Artwork label (modules)
Define the Artist class in Artist.py with a constructor to initialize an artist's information. The constructor should by default initialize the artist's name to "None" and the years of birth and death to 0.

Define the Artwork class in Artwork.py with a constructor to initialize an artwork's information. The constructor should by default initialize the title to "None", the year created to 0, and the artist to use the Artist default constructor parameter values. Add an import statement to import the Artist class.

Add import statements to main.py to import the Artist and Artwork classes.

Ex: If the input is:

Pablo Picasso
1881
1973
Three Musicians
1921
the output is:

Artist: Pablo Picasso (1881-1973)
Title: Three Musicians, 1921
If the input is:

Brice Marden
1938
-1
Distant Muses
2000
the output is:

Artist: Brice Marden, born 1938
Title: Distant Muses, 2000
'''

#main.py
from Artist import *
from Artwork import *

if __name__ == "__main__":
    user_artist_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)
    new_artwork = Artwork(user_title, user_year_created, user_artist)
    new_artwork.print_info()

#artist.py
class Artist:
    def __init__(self, name="None", birth_year=0, death_year=0):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def print_info(self):
        if self.death_year == -1:
            print('Artist: {}, born {}'.format(self.name, self.birth_year))
        else:
            print('Artist: {} ({}-{})'.format(self.name, self.birth_year, self.death_year))

#artwork.py
from Artist import *


class Artwork:
    def __init__(self, title="None", year_created=0, artist=Artist()):
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def print_info(self):
        self.artist.print_info()
        print("Title: %s, %d" % (self.title, self.year_created))
