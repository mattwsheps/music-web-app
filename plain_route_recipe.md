# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
POST /albums
    title: string
    release_year: number (str)
    artist_id: number (str)

GET /artists

POST /artists
    name: string
    genre: string
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# Scenario 1

# POST /albums
#   title='Voyage'
#   release_year=2022
#   artist_id=5

# Expected response (200 OK)
"""
""" (no content)

# GET /albums
# Expected response (200 OK)
"""
Album(1, "Red", 2022, 1),
Album(2, "Blue Note Sessions", 2021, 2),
Album(3, "Back in Black", 1980, 3),
Album(4, "Golden Fields", 2019, 4),
Album(5, "Voyage", 2022, 5)
"""

# Scenario 2

# POST /albums
# Expected response (400 Bad Request)
"""
You must submit a title, release_year and artist_id
"""

# Scenario 3

# GET /artists
# Expected response (200 OK)
"""
Taylor Swift, Nigel Kennedy, AC/DC, Pixies
"""

# Scenario 4

# POST /artists
#   name: Wild nothing
#   genre: Indie
# Expected response (200 OK)
"""(no content)
"""

# GET /artists
# Expected response (200 OK)
"""
Taylor Swift, Nigel Kennedy, AC/DC, Pixies, Wild nothing
"""

# Scenario 5
# POST /artists
# Expected response (400 Bad request)
"""
You must submit an artist name and genre!
"""


```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
POST /albums
Expected response (200 OK):
(No content)
"""
def test_post_albums(db_connection, web_client):
    response = web_client.post('/albums')


"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
