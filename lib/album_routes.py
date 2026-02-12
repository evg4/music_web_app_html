from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from flask import request


def apply_album_routes(app):
    @app.route('/albums', methods=['GET'])
    def get_albums(): 
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        return ", ".join([str(album) for album in repository.all()])
    
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
        