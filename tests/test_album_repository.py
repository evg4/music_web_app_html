from lib.album_repository import AlbumRepository
from lib.album import Album

def test_create_album_with_correct_data(db_connection):
    db_connection.seed('seeds/albums_table.sql')
    ar = AlbumRepository(db_connection)
    album = {'title': 'My title', 'release_year': 1990, "artist_id": 2}
    assert ar.create(album) == 'Album successfully created.'
    assert ar.all() == [Album(1, 'Title 1', 1998, 3), Album(2, 'Title 2', 2007, 4), Album(3, 'Another title', 2023, 1), Album(4, 'Final title', 1956, 3), Album(5, 'My title', 1990, 2)]
    
def test_create_album_with_no_data(db_connection):
    db_connection.seed('seeds/albums_table.sql')
    ar = AlbumRepository(db_connection)
    album = {}
    assert ar.create(album) == 'Please provide a title, release year and artist ID.'
    assert ar.all() == [Album(1, 'Title 1', 1998, 3), Album(2, 'Title 2', 2007, 4), Album(3, 'Another title', 2023, 1), Album(4, 'Final title', 1956, 3)]

def test_create_album_with_partial_data(db_connection):
    db_connection.seed('seeds/albums_table.sql')
    ar = AlbumRepository(db_connection)
    album = {'title': 'Great title'}
    assert ar.create(album) == 'Please provide a title, release year and artist ID.'
    assert ar.all() == [Album(1, 'Title 1', 1998, 3), Album(2, 'Title 2', 2007, 4), Album(3, 'Another title', 2023, 1), Album(4, 'Final title', 1956, 3)]

def test_find_album_id_1(db_connection):
    db_connection.seed('seeds/albums_table.sql')
    ar = AlbumRepository(db_connection)
    album1 = ar.find(1)
    assert album1 == Album(1, 'Title 1', 1998, 3)

def test_find_album_with_artist_name(db_connection):
    db_connection.seed('seeds/albums_table.sql')
    ar = AlbumRepository(db_connection)
    album1 = ar.find_with_artist_name(1)
    assert album1[0] == Album(1, 'Title 1', 1998, 3)
    assert album1[1] == 'Taylor Swift'

'''
def test_valid_data_with_valid_data(db_connection):
    ar = AlbumRepository(db_connection)
    album = {'title': 'My title', 'release_year': 1990, "artist_id": 2}
    assert ar.__valid_data(album) == {'title': 'My title', 'release_year': 1990, "artist_id": 2}
'''

'''
the above test will fail because it says the class AlbumRepository has no attribute __valid_data. That's because I have preprended it with __, signifying that it should not be accessed outside of the class.

If I amend to valid_data it works, but that then changes the design of __valid_data.

The behaviour of __valid_data is being tested in the create method anyway so I know that it works.
'''