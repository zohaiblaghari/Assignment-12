def add_song(songs_dict):
    title = input("Enter the song title:")
    artist = input("Enter the artist:")
    genre = input("Enter the genre:")
    songs_dict[title] = {"artist": artist, "genre": genre}
    
def search_song(songs_dict, search_term):
    for title, details in songs_dict.items():
        if search_term.lower() in title.lower() or search_term.lower() in details['artist'].lower() or search_term.lower() in details['genre'].lower():
            print(f"Title: {title}, Artist: {details['artist']}, Genre: {details['genre']}")
            return
    print(f"Song not found.")

def main():
    songs = {}
    while True:
        print("\n1. Add a song\n2. Search for a song\n3. Exit")
        choice = input("Enter your choice:")
        if choice == "1":
            add_song(songs)
        elif choice == "2":
            search_term = input("Enter the song title, artist, or genre to search:")
            search_song(songs, search_term)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


        