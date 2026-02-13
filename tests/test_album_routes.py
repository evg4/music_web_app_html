from lib.album import Album
from playwright.sync_api import Page, expect

def test_get_albums(db_connection, web_client, page, test_web_address):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    #assert response.data.decode('utf-8') == "Album(1, Title 1, 1998, 3), Album(2, Title 2, 2007, 4), Album(3, Another title, 2023, 1), Album(4, Final title, 1956, 3)"
    page.goto(f"http://{test_web_address}/albums")
    h1 = page.locator("h1")
    a = page.locator("a")
    p = page.locator("p")
    expect(h1).to_have_text("Albums")
    expect(a).to_have_text(['\nTitle: Title 1\nReleased: 1998\n', '\nTitle: Title 2\nReleased: 2007\n', '\nTitle: Another title\nReleased: 2023\n', '\nTitle: Final title\nReleased: 1956\n', 'Home'])
    expect(p).to_have_text(['Title: Title 1 Released: 1998', 'Title: Title 2 Released: 2007', 'Title: Another title Released: 2023', 'Title: Final title Released: 1956'])

def test_clicking_album_shows_page(db_connection, page, test_web_address):
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.get_by_text('Title 1').click()
    h1 = page.locator("h1")
    p = page.locator("p")
    expect(h1).to_have_text("Title 1")
    expect(p).to_have_text("Release year: 1998 Artist: Taylor Swift")
    page.goto(f"http://{test_web_address}/albums")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Albums")
    page.get_by_text('Another title').click()
    h1 = page.locator("h1")
    expect(h1).to_have_text("Another title")
    p = page.locator("p")
    expect(p).to_have_text("Release year: 2023 Artist: Pixies")


    # Notice that if I'm asserting on the a tag, I need the \n. But if I assert on the p, there are no \n.

    # below is an alernative way. to_have_text needs an exact match, whereas to_contain_text just needs a partial string (i.e. contained within it). We can also access a specific tag with .nth(0) rather than asserting them all in a list.

    # p = page.locator("div p").nth(0)
    # expect(p).to_contain_text("Title: Title 1")
    # expect(p).to_contain_text("Released: 1998")


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
    

