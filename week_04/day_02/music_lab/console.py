import pdb 
from models.artist import Artist 
from models.album import Album 
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# artist_1 = Artist("Kylie", "Minogue")
# artist_2 = Artist("Micheal", "Buble")

# artist_repository.save(artist_1)
# artist_repository.save(artist_2)

# album_1 = Album("Lovers", "Pop", artist_1)
# album_2 = Album("Crazy Love", "Jazz", artist_2)
# album_3 = Album("It's Time", "Jazz", artist_2)
# album_4 = Album("Christmas", "Christmas music", artist_2)

# album_repository.save(album_1)
# album_repository.save(album_2)
# album_repository.save(album_3)
# album_repository.save(album_4)

# res = album_repository.select_all()
# for album in res:
#     print(album.__dict__)

# res = artist_repository.select_all()
# for artist in res:
#     print(artist.__dict__)

found_albums = album_repository.select_by_artist_id(2)
for album in found_albums:
    print(album.__dict__)

artist = album_repository.select_artist_by_album_id(1)
print(artist.__dict__)