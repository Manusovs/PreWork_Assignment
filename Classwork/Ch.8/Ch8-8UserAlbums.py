# if "3" != ' ':
#     print("t")
# else: 
#     print ("f")


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
    if Album["# of tracks"] != " ":
        Album = make_album(art_name,alb_title, track_num)
        print(f'{Album["# of tracks"]} tracks on {Album["album title"]}')
    else: 
        print("tracks not listed")
flag = True

while flag == True:
    print("enter 'q' at any time to exit program")
    art_name = input("Please enter artist name:  ")
    if art_name == "q":
        break
    alb_title = input("Plese enter the album's title:  ")
    if alb_title == "q":
        break
    track_num = input("Plese enter the number of tracks in the album:  ")
    if track_num == "q":
        break
    make_album(art_name,alb_title,track_num)
    call_tracks("i")