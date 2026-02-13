from lib.album import Album
from playwright.sync_api import Page, expect

def test_get_albums(db_connection, web_client, page, test_web_address):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    #assert response.data.decode('utf-8') == "Album(1, Title 1, 1998, 3), Album(2, Title 2, 2007, 4), Album(3, Another title, 2023, 1), Album(4, Final title, 1956, 3)"
    page.goto(f"http://{test_web_address}/albums")
    h1 = page.locator("h1")
    p = page.locator("div p").nth(0)
    expect(h1).to_have_text("Albums")
    expect(p).to_contain_text("Title: Title 1")
    expect(p).to_contain_text("Released: 1998")

'''
- it's easier to put all SQL queries in one file and call it e.g. 'music library' rather than splitting up into each table. This way works, but if I have a test which involves more than one table, I'll have to seed it twice.
- if there are multiple of the same elements on a page, you can still access them with page.locator, then just assert them in a list, i.e.
p_tags = page.locator("p")
expect(p).to_have_text(["p1 text", "p2 text", "p3 text])
- Kay's version of the above test doesn't pass in web_client, and doesn't bother asserting the status_code.
'''

def test_get_one_album(db_connection, web_client, page, test_web_address):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.get('/albums/1')
    assert response.status_code == 200
    page.goto(f"http://{test_web_address}/albums/1")
    h1 = page.locator("h1")
    p = page.locator("p")
    expect(h1).to_have_text("Title 1")
    expect(p).to_have_text("Release year: 1998\nArtist: Taylor Swift")
    

def test_post_album(db_connection, web_client, page, test_web_address):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.post('/albums', data = {'title': 'Voyage', 'release_year': 2022, 'artist_id': 2})
    assert response.status_code == 201
    assert response.data.decode('utf-8') == "Album successfully created."
    response_2 = web_client.get('/albums')
    assert response_2.status_code == 200
    page.goto(f"http://{test_web_address}/albums")
    h1 = page.locator("h1")
    p = page.locator("div p").nth(4)
    expect(h1).to_have_text("Albums")
    expect(p).to_contain_text("Title: Voyage")
    expect(p).to_contain_text("Released: 2022")
    #assert response_2.data.decode('utf-8') == "Album(1, Title 1, 1998, 3), Album(2, Title 2, 2007, 4), Album(3, Another title, 2023, 1), Album(4, Final title, 1956, 3), Album(5, Voyage, 2022, 2)"
    

def test_post_album_no_params(db_connection, web_client):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.post('/albums', data = {})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Please enter a title, release year and artist id"
    
