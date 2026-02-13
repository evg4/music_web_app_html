from lib.artist import Artist
from lib.album import Album

class ArtistRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        artist_rows = self._connection.execute("SELECT * FROM artists")
        return [Artist(row['id'], row['name'], row['genre']) for row in artist_rows]
    
    def create(self, artist):
        self._connection.execute("INSERT INTO artists (name, genre) VALUES (%s, %s)", [artist['name'], artist['genre']])
        return "Artist added to database."
    
    def find(self, id):
        artist = self._connection.execute("SELECT * FROM artists WHERE id = %s", [id])[0]
        return Artist(artist['id'], artist['name'], artist['genre'])
    
    def find_with_albums(self, artist_id):
        rows = self._connection.execute("SELECT artists.id AS artist_id, name, genre, albums.id AS album_id, title, release_year FROM artists JOIN albums ON artist_id = artists.id WHERE artist_id = %s", [artist_id])
        artist = Artist(rows[0]['artist_id'], rows[0]['name'], rows[0]['genre'])
        albums = []
        for album in rows:
            albums.append(Album(album['album_id'], album['title'], album['release_year'], album['artist_id']))
        return artist, albums