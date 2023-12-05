from lib.artist_repository import *
from lib.artist import *

"""
When I call get #all
I get a list of all artists in the artists table
"""
def test_list_all_artists(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = ArtistRepository(db_connection)

    artists = repository.all()
    assert artists == [
        Artist(1, 'Taylor Swift', 'Pop'),
        Artist(2, 'Nigel Kennedy', 'Classical'),
        Artist(3, 'AC/DC', 'Rock'),
        Artist(4, 'Pixies', 'Indie')
    ]

"""
When I call #create
I create an artist in the database
And can see it in #all
"""
def test_create_artist(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(None, "Wild nothing", "Indie")
    repository.create(artist)
    artists = repository.all()
    assert artists == [
        Artist(1, 'Taylor Swift', 'Pop'),
        Artist(2, 'Nigel Kennedy', 'Classical'),
        Artist(3, 'AC/DC', 'Rock'),
        Artist(4, 'Pixies', 'Indie'),
        Artist(5, 'Wild nothing', 'Indie')
    ]