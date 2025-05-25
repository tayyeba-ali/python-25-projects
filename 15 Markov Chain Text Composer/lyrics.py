import os
import lyricsgenius

# Initialize Genius API
genius = lyricsgenius.Genius("wGY75GiYuUO-toTOYAQ_NzTXHx4LGXvBpqPL40bGVlVbkS6VAiJncei1E4ijYCvk")

def save_lyrics(songs, artist_name, album_name="unknown_album"):
    # Clean artist name for folder name
    artist_folder = '_'.join(artist_name.split(' '))
    save_path = f'songs/{artist_folder}'
    
    # Create folder if it doesn't exist
    os.makedirs(save_path, exist_ok=True)

    for i, song_title in enumerate(songs, start=1):
        song = genius.search_song(song_title, artist_name)
        if song:
            lyrics = song.lyrics
            # Clean file name
            cleaned_title = '-'.join(''.join(song_title.split("'")).split(' '))
            filename = f"{i}_{album_name}_{cleaned_title}.txt"
            with open(os.path.join(save_path, filename), 'w', encoding='utf-8') as f:
                f.write(lyrics)
            print(f"Saved: {filename}")
        else:
            print(f"Song not found: {song_title}")

if __name__ == '__main__':
    songs = [
        'the box',
        'down below',
        'project dreams',
        'die young',
        'boom boom room',
        'high fashion',
        'roll dice',
        'war baby',
        'every season'
    ]
    save_lyrics(songs, 'Roddy Ricch', 'Please_Excuse_Me_For_Being_Antisocial')
