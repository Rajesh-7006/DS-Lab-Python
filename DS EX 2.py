class Song:
    def __init__(self, title):
        self.title = title
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title):
        new_song = Song(title)
        if self.head is None:
            self.head = new_song
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_song
        print(f"'{title}' added to playlist.")

    def delete_song(self, title):
        temp = self.head
        prev = None
        while temp:
            if temp.title == title:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                print(f"'{title}' deleted from playlist.")
                return
            prev = temp
            temp = temp.next
        print(f"'{title}' not found.")

    def show_playlist(self):
        if self.head is None:
            print("Playlist is empty.")
            return
        temp = self.head
        print("Playlist:")
        while temp:
            print("-", temp.title)
            temp = temp.next

playlist = Playlist()

while True:
    print("\n1. Add Song  2. Delete Song  3. Show Playlist  4. Exit")
    choice = input("Choose: ")

    if choice == '1':
        song = input("Enter song name: ")
        playlist.add_song(song)
    elif choice == '2':
        song = input("Enter song to delete: ")
        playlist.delete_song(song)
    elif choice == '3':
        playlist.show_playlist()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
'''
1. Add Song  2. Delete Song  3. Show Playlist  4. Exit
Choose: 1
Enter song name: Hi Sona
'Hi Sona' added to playlist.

1. Add Song  2. Delete Song  3. Show Playlist  4. Exit
Choose: 1
Enter song name: Power House
'Power House' added to playlist.

1. Add Song  2. Delete Song  3. Show Playlist  4. Exit
Choose: 1
Enter song name: Mobsta
'Mobsta' added to playlist.

1. Add Song  2. Delete Song  3. Show Playlist  4. Exit
Choose: 3
Playlist:
- Hi Sona
- Power House
- Mobsta

1. Add Song  2. Delete Song  3. Show Playlist  4. Exit
Choose: 2
Enter song to delete: Hi Sona
'Hi Sona' deleted from playlist.

1. Add Song  2. Delete Song  3. Show Playlist  4. Exit
Choose: 3
Playlist:
- Power House
- Mobsta

1. Add Song  2. Delete Song  3. Show Playlist  4. Exit
Choose: 4
Exiting…
'''