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
        if self.__valid_data(album):
            title = album['title']
            release_year = album['release_year']
            artist_id = album['artist_id']
            self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [title, release_year, artist_id])
            return 'Album successfully created.'
        else:
            return 'Please provide a title, release year and artist ID.'
    def __valid_data(self, album):
        return album.get('title', False) and album.get('release_year', False) and album.get('artist_id', False) and album
    
    '''
    My title and 1990 and 2
    '''