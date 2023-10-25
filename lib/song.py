class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self._name = name
        self._artist = artist
        self._genre = genre
        Song.count +=1 
        if not (self._genre in Song.genres):
            Song.genres.append(self._genre)

        if not(self._genre in Song.genre_count):
            Song.genre_count[self._genre] = 1
        else:
            Song.genre_count[self._genre] += 1
        
        if not (self._artist in Song.artists):
            Song.artists.append(self._artist)

        if not(self._artist in Song.artist_count):
            Song.artist_count[self._artist] = 1
        else:
            Song.artist_count[self._artist] += 1
        
    @property
    def name(self):
        return self._name
    
    @property
    def artist(self):
        return self._artist
    
    @property
    def genre(self):
        return self._genre
    
    @name.setter
    def name(self,name):
        self._name = name
    
    @artist.setter
    def artist(self,artist):
        self._artist = artist
    
    @genre.setter
    def genre(self,genre):
        self._genre = genre
    

# You can now access the count property directly
print(Song.count)  # This will print the count of all songs