from lib.artist import Artist

def test_artist_initialises():
    artist = Artist(1, 'Taylor Swift', 'Pop')
    assert artist.id == 1
    assert artist.name == 'Taylor Swift'
    assert artist.genre == 'Pop'

def test_formatting():
    artist = Artist(1, 'Taylor Swift', 'Pop')
    assert str(artist) == 'Artist(1, Taylor Swift, Pop)'

def test_equality():
    artist1 = Artist(1, 'Taylor Swift', 'Pop')
    artist2 = Artist(1, 'Taylor Swift', 'Pop')
    assert artist1 == artist2