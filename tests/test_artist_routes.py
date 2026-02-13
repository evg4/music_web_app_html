def test_get_artists(db_connection, web_client):
    db_connection.seed('seeds/artists_table.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"


def test_post_artist_Wild_nothing(db_connection, web_client):
    db_connection.seed('seeds/artists_table.sql')
    response_1 = web_client.post('/artists', data={'name':'Wild nothing', 'genre':'indie'})
    assert response_1.status_code == 200
    assert response_1.data.decode('utf-8') == "Artist added."
    response_2 = web_client.get('/artists')
    assert response_2.status_code == 200
    assert response_2.data.decode('utf-8') =="Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"


def test_post_artist_no_data(db_connection, web_client):
    db_connection.seed('seeds/artists_table.sql')
    response_1 = web_client.post('/artists', data={})
    assert response_1.status_code == 400
    assert response_1.data.decode('utf-8') == 'Please provide a name and genre.'
    response_2 = web_client.get('/artists')
    assert response_2.status_code == 200
    assert response_2.data.decode('utf-8') =="Pixies, ABBA, Taylor Swift, Nina Simone"


def test_post_artist_partial_data(db_connection, web_client):
    db_connection.seed('seeds/artists_table.sql')
    response_1 = web_client.post('/artists', data={'name': 'Sabrina Carpenter'})
    assert response_1.status_code == 400
    assert response_1.data.decode('utf-8') == 'Please provide a name and genre.'
    response_2 = web_client.get('/artists')
    assert response_2.status_code == 200
    assert response_2.data.decode('utf-8') =="Pixies, ABBA, Taylor Swift, Nina Simone"
    