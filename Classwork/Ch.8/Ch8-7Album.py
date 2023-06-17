def make_album(name , title, tracks = "" ):
    if tracks != "":    
        music_album = {"artist" : name,
                    "album title" : title,
                    "# of tracks": tracks}
    else:
        music_album = {"artist" : name,
                   "album title" : title}
       
    return music_album


def call_tracks(Album):
    Album = make_album("a","b", 160)
    print(f'{Album["# of tracks"]}')

call_tracks("Hello Hello")
