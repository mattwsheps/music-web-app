"""
When I call GET /albums
I get a list of albums back
"""
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "" \
        "Album(1, Red, 2022, 1)\n" \
        "Album(2, Blue Note Sessions, 2006, 2)\n" \
        "Album(3, Back in Black, 1980, 3)\n" \
        "Album(4, Death to the Pixies, 1997, 4)"

"""
When I call POST /albums with album info
That album is now in the list in /GET albums
"""
def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    post_response = web_client.post("/albums", data={
        'title': "Voyage", 
        "release_year": '2022', 
        "artist_id": '4'
        })
    
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "" \
        "Album(1, Red, 2022, 1)\n" \
        "Album(2, Blue Note Sessions, 2006, 2)\n" \
        "Album(3, Back in Black, 1980, 3)\n" \
        "Album(4, Death to the Pixies, 1997, 4)\n" \
        "Album(5, Voyage, 2022, 4)"

"""
When I call POST /albums with no album info
It raises the error
'You must submit a title, release_year and artist_id'
"""
def test_post_albums_with_no_data(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    post_response = web_client.post("/albums")
    
    assert post_response.status_code == 400
    assert post_response.data.decode("utf-8") == "" \
        "You must submit a title, release_year and artist_id"

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "" \
        "Album(1, Red, 2022, 1)\n" \
        "Album(2, Blue Note Sessions, 2006, 2)\n" \
        "Album(3, Back in Black, 1980, 3)\n" \
        "Album(4, Death to the Pixies, 1997, 4)"

"""
When I call GET /artists
I get a list of artists back
"""
def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "" \
        "Taylor Swift, Nigel Kennedy, AC/DC, Pixies"

"""
When I call POST /artists with name, genre
The artist is seen in GET /artists
"""
def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    post_response = web_client.post('/artists', data={
        'name': 'Wild nothing',
        'genre': 'Indie'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode("utf-8") == ""

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "" \
        "Taylor Swift, Nigel Kennedy, AC/DC, Pixies, Wild nothing"

"""
When I call POST /artists with no name or genre
It raises the error:
'You must submit an artist name and genre!'
"""
def test_post_artists_with_no_data(db_connection, web_client):
    db_connection.seed("seeds/music_web_app.sql")
    post_response = web_client.post('/artists')
    assert post_response.status_code == 400
    assert post_response.data.decode("utf-8") == "" \
        "You must submit an artist name and genre!"

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode("utf-8") == "" \
        "Taylor Swift, Nigel Kennedy, AC/DC, Pixies"

