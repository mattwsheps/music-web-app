from lib.artist import *

"""
Artist constructs with an id, name, genre
"""
def test_artist_constructs():
    artist = Artist(1, "Test Name", "Test Genre")
    assert artist.id == 1
    assert artist.name == "Test Name"
    assert artist.genre == "Test Genre"

"""
Two identical artists can equal each other
"""
def test_artists_are_equal():
    artist1 = Artist(1, "Test Name", "Test Genre")
    artist2 = Artist(1, "Test Name", "Test Genre")
    assert artist1 == artist2

"""
We can format artists to strings nicely
"""
def test_artists_formats_nicely():
    artist = Artist(1, "Test Name", "Test Genre")
    assert str(artist) == "Artist(1, Test Name, Test Genre)"