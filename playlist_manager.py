playlist = []
print(" Welcome to Playlist ")
for i in range(10):
    song = input(f"Enter song name {i+1}: ")
    playlist.append(song)
print("\nYour Playlist:")
print(playlist)
print("\nYour Playlist in Reverse Order:")
print(playlist[::-1])
