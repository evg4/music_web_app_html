from lib.album import Album

class AlbumRepository:
    def __init__(self, db_connection):
        self._connection = db_connection
    def all(self):
        rows = self._connection.execute('SELECT * FROM albums')
        albums = []
        for row in rows:
            item = Album(row['id'], row['title'], row['release_year'], row['artist_id'])
            albums.append(item)
        return albums
    def create(self, album):
        title = album['title']
        release_year = album['release_year']
        artist_id = album['artist_id']
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [title, release_year, artist_id])
        return 'Album successfully created.'