import lyricsgenius as lg

filename = input('Enter a file:') or 'Lyrics.txt'
file = open(filename,"w+")

genius = lg.Genius('Client_Access_Token_Goes_Here',skip_non_songs=True,excluded_terms=["(Remix)","(Live)"], remove_section_headers = True)
input_string = input("Enter name of Artists separated  by spaces:")
artists = input_string.split("")
def get_lyrics(arr,max_song):
    c=0
    for name in arr:
        try:
            songs = (genius.search_artist(name,max_songs=max_song,sort='popularity')).songs
            s =[song.lyrics for song in songs]
            file.write("\n\n <|endoftext> \n\n".join(s))
            c += 1
            print(f"Song grabbed:{lens}")
        except:
            print(f"some exception at {name}:{c}")


get_lyrics(artists,3)
