from lib.album import Album

"""
Album constructs with an id, title, release_year and artist_id
"""
def test_album_constructs():
    album = Album(1, "Test Album", 2000, 1)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.release_year == 2000
    assert album.artist_id == 1

"""
We can format Albums to strings nicely
"""
def test_Albums_format_nicely():
    album = Album(1, "Test Album", 2000, 1)
    assert str(album) == "Album(1, Test Album, 2000, 1)"
    # Try commenting out the `__repr__` method in lib/Album.py
    # And see what happens when you run this test again.

"""
We can compare two identical Albums
And have them be equal
"""
def test_Albums_are_equal():
    album1 = Album(1, "Test Album", 2000, 1)
    album2 = Album(1, "Test Album", 2000, 1)
    assert album1 == album2