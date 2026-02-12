from lib.artist import Artist

class ArtistRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        artist_rows = self._connection.execute("SELECT * FROM artists")
        return [Artist(row['id'], row['name'], row['genre']) for row in artist_rows]
    
    def create(self, artist):
        self._connection.execute("INSERT INTO artists (name, genre) VALUES (%s, %s)", [artist['name'], artist['genre']])
        return "Artist added to database."