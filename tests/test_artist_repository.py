from lib.artist_repository import ArtistRepository
from lib.artist import Artist

def test_get_all_artists(db_connection):
    db_connection.seed('seeds/artists_table.sql')
    repository = ArtistRepository(db_connection)
    result = repository.all()
    assert result == [Artist(1, 'Pixies', 'Rock'), Artist(2, 'ABBA', 'Pop'), Artist(3, 'Taylor Swift', 'Pop'), Artist(4, 'Nina Simone', 'Jazz')]

def test_create_artist(db_connection):
    db_connection.seed('seeds/artists_table.sql')
    repository = ArtistRepository(db_connection)
    artist = {'name': 'Harry Styles', 'genre': 'Pop'}
    assert repository.create(artist) == "Artist added to database."
    result = repository.all()
    assert result == [Artist(1, 'Pixies', 'Rock'), Artist(2, 'ABBA', 'Pop'), Artist(3, 'Taylor Swift', 'Pop'), Artist(4, 'Nina Simone', 'Jazz'), Artist(5, 'Harry Styles', 'Pop')]


