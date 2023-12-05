from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When I call #all
I get all the albums in the albums table
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()
    assert albums == [
            Album(1, "Red", 2022, 1),
            Album(2, "Blue Note Sessions", 2006, 2),
            Album(3, "Back in Black", 1980, 3), 
            Album(4, "Death to the Pixies", 1997, 4)
        ]

"""
When I call #create
I create an album in the database
And I can see it back in #all
"""
def test_create(db_connection):
    db_connection.seed("seeds/music_web_app.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, "Test Album", 2000, 2)
    repository.create(album)
    albums = repository.all()
    assert albums == [
            Album(1, "Red", 2022, 1),
            Album(2, "Blue Note Sessions", 2006, 2),
            Album(3, "Back in Black", 1980, 3), 
            Album(4, "Death to the Pixies", 1997, 4),
            Album(5, "Test Album", 2000, 2)
        ]