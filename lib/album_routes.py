from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
from flask import request, render_template


def apply_album_routes(app):
    @app.route('/albums', methods=['GET'])
    def get_albums(): 
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        albums = repository.all()
        return render_template('albums.html', albums=albums)
        #return ", ".join([str(album) for album in repository.all()])
    
    @app.route('/albums/<int:id>')
    def get_album_by_id(id):
        connection = get_flask_database_connection(app)
        album_repository = AlbumRepository(connection)
        artist_repository = ArtistRepository(connection)
        album = album_repository.find(id)
        artist = artist_repository.find(album.artist_id)
        return render_template('album.html', album=album, artist_name=artist.name)

    @app.route('/albums', methods=['POST'])
    def create_album():
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        if not request.form:
            return "Please enter a title, release year and artist id", 400
        title = request.form['title']
        release_year = request.form['release_year']
        artist_id = request.form['artist_id']
        album = {'title': title, 'release_year': release_year, 'artist_id': artist_id}
        return repository.create(album), 201