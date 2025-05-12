import os
import re
import string
import random
from graph import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path, 'rb') as file:
        text = file.read().decode("utf-8") 

        # remove [verse 1: artist]
        # include the following line if you are doing song lyrics
        text = re.sub(r'\[(.+)\]', ' ', text)

        text = ' '.join(text.split())
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split() # split by whitespace
    words = words[:1000]  # limit to first 1000 words if you want
    return words

def make_graph(words):
    g = Graph()
    prev_word = None
    for word in words:
        word_vertex = g.get_vertex(word)
        
        if prev_word:  # if there's a previous word
            prev_word.increment_edge(word_vertex)
            
        prev_word = word_vertex

    g.generate_probability_mappings()
    return g

def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    return composition

def main(artist):
    words = []
    artist_dir = os.path.join('songs', artist)
    
    if not os.path.exists(artist_dir):
        raise Exception(f"Directory not found: {artist_dir}")
    
    for song_file in os.listdir(artist_dir):
        if song_file.startswith('.'):  
            continue
        song_path = os.path.join(artist_dir, song_file)
        words.extend(get_words_from_text(song_path))
        
    g = make_graph(words)
    composition = compose(g, words, 100)
    print(' '.join(composition))

if __name__ == '__main__':
    main('billie_eilish')  