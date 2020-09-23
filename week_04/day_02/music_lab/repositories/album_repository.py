from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository

def save(album):
    sql = f"INSERT INTO albums(title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums

def select_by_artist_id(artist_id):
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist_id]
    results = run_sql(sql, values)
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums

def select_artist_by_album_id(id):
    album = None 
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    if result is not None:
        artist = artist_repository.select(result['artist_id'])
    return artist
