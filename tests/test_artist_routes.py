from playwright.sync_api import Page, expect

def test_get_artists(db_connection, web_client, page, test_web_address):
    db_connection.seed('seeds/artists_table.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    #assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"
    page.goto(f'http://{test_web_address}/artists')
    h1 = page.locator('h1')
    artists = page.locator('li')
    expect(h1).to_have_text("Artists")
    expect(artists).to_have_text(["Pixies", "ABBA", "Taylor Swift", "Nina Simone"])

def test_clicking_artist_goes_to_that_page(db_connection, web_client, page, test_web_address):
    db_connection.seed('seeds/artists_table.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    #assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"
    page.goto(f'http://{test_web_address}/artists')
    h1 = page.locator('h1')
    artists = page.locator('li')
    expect(h1).to_have_text("Artists")
    expect(artists).to_have_text(["Pixies", "ABBA", "Taylor Swift", "Nina Simone"])
    page.get_by_text('Taylor Swift').click()
    h1 = page.locator("h1")
    genre = page.locator("p").nth(0)
    h2 = page.locator("h2")
    albums = page.locator("li")
    expect(h1).to_have_text("Taylor Swift")
    expect(genre).to_have_text("Genre: Pop")
    expect(h2).to_have_text("Albums:")
    expect(albums).to_have_text(["Title 1 (1998)", "Final title (1956)"])

def test_clicking_missing_artist_displays_message(db_connection, page, test_web_address):
    db_connection.seed('seeds/artists_table.sql')
    db_connection.seed('seeds/albums_table.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.get_by_text("ABBA").click()
    text = page.locator("p")
    print(text)
    expect(text).to_have_text("Artist not found")

def test_back_button_goes_to_artists_page(db_connection, page, test_web_address):
    db_connection.seed('seeds/artists_table.sql')
    page.goto(f"http://{test_web_address}/artists/1")
    page.get_by_text("Back to all artists").click()
    h1 = page.locator("h1")
    expect(h1).to_have_text("Artists")

def test_get_artist_by_valid_id(db_connection, web_client, page, test_web_address):
    db_connection.seed('seeds/artists_table.sql')
    response = web_client.get('/artists/1')
    assert response.status_code == 200
    page.goto(f'http://{test_web_address}/artists/1')
    h1 = page.locator("h1")
    genre = page.locator("p").nth(0)
    h2 = page.locator("h2")
    albums = page.locator("li")
    expect(h1).to_have_text("Pixies")
    expect(genre).to_have_text("Genre: Rock")
    expect(h2).to_have_text("Albums:")
    expect(albums).to_have_text(['Another title (2023)'])


def test_post_artist_Wild_nothing(db_connection, web_client, page, test_web_address):
    db_connection.seed('seeds/artists_table.sql')
    response_1 = web_client.post('/artists', data={'name':'Wild nothing', 'genre':'indie'})
    assert response_1.status_code == 200
    assert response_1.data.decode('utf-8') == "Artist added."
    response_2 = web_client.get('/artists')
    assert response_2.status_code == 200
    #assert response_2.data.decode('utf-8') =="Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"
    page.goto(f'http://{test_web_address}/artists')
    h1 = page.locator('h1')
    artists = page.locator('li')
    expect(h1).to_have_text("Artists")
    expect(artists).to_have_text(["Pixies", "ABBA", "Taylor Swift", "Nina Simone", "Wild nothing"])


def test_post_artist_no_data(db_connection, web_client, page, test_web_address):
    db_connection.seed('seeds/artists_table.sql')
    response_1 = web_client.post('/artists', data={})
    assert response_1.status_code == 400
    assert response_1.data.decode('utf-8') == 'Please provide a name and genre.'
    response_2 = web_client.get('/artists')
    assert response_2.status_code == 200
    #assert response_2.data.decode('utf-8') =="Pixies, ABBA, Taylor Swift, Nina Simone"
    page.goto(f'http://{test_web_address}/artists')
    h1 = page.locator('h1')
    artists = page.locator('li')
    expect(h1).to_have_text("Artists")
    expect(artists).to_have_text(["Pixies", "ABBA", "Taylor Swift", "Nina Simone"])


def test_post_artist_partial_data(db_connection, web_client, page, test_web_address):
    db_connection.seed('seeds/artists_table.sql')
    response_1 = web_client.post('/artists', data={'name': 'Sabrina Carpenter'})
    assert response_1.status_code == 400
    assert response_1.data.decode('utf-8') == 'Please provide a name and genre.'
    response_2 = web_client.get('/artists')
    assert response_2.status_code == 200
    #assert response_2.data.decode('utf-8') =="Pixies, ABBA, Taylor Swift, Nina Simone"
    page.goto(f'http://{test_web_address}/artists')
    h1 = page.locator('h1')
    artists = page.locator('li')
    expect(h1).to_have_text("Artists")
    expect(artists).to_have_text(["Pixies", "ABBA", "Taylor Swift", "Nina Simone"])
    