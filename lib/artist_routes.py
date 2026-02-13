from lib.database_connection import get_flask_database_connection
from lib.artist_repository import ArtistRepository
from flask import request, render_template

def apply_artist_routes(app):
    @app.route('/artists')
    def get_artists():
        connection = get_flask_database_connection(app)
        repository = ArtistRepository(connection)
        return ", ".join([artist.name for artist in repository.all()])
    
    @app.route('/artists/<int:id>')
    def get_artist_by_id(id):
        connection = get_flask_database_connection(app)
        repository = ArtistRepository(connection)
        result = repository.find_with_albums(id)
        artist = result[0]
        albums = result[1]
        return render_template('artist.html', artist=artist, albums=albums)

    @app.route('/artists', methods=['POST'])
    def create_artist():
        connection = get_flask_database_connection(app)
        repository = ArtistRepository(connection)
        if not valid_data(request):
            return "Please provide a name and genre.", 400
        name = request.form['name']
        genre = request.form['genre']
        artist = {'name': name, 'genre': genre}
        repository.create(artist)
        return "Artist added."
        
    def valid_data(request):
        return request.form and request.form.get('name', False) and request.form.get('genre', False)