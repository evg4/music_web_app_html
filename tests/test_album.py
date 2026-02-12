from lib.album import Album

def test_album_initialises():
    album = Album(1, 'Title', 1990, 2)
    assert album.id == 1
    assert album.title == 'Title'
    assert album.release_year == 1990
    assert album.artist_id == 2

def test_equality():
    album1 = Album(1, 'Title', 1990, 2)
    album2 = Album(1, 'Title', 1990, 2)
    assert album1 == album2

def test_formatting():
    album = Album(1, 'Title', 1990, 2)
    assert str(album) == 'Album(1, Title, 1990, 2)'