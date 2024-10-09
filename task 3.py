import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playlist = []
        self.current_index = 0

    def add_to_playlist(self, song):
        self.playlist.append(song)

    def play(self):
        if not pygame.mixer.music.get_busy() and self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    def next_song(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def previous_song(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def create_playlist(self, songs):
        self.playlist = songs

if __name__ == "__main__":
    player = MusicPlayer()

    # Example usage
    player.add_to_playlist(r"c:\Users\Harika Yarra\Music\[iSongs.info] 01 - Chiru Chiru Chiru.mp3")
    player.add_to_playlist(r"c:\Users\Harika Yarra\Music\[iSongs.info] 01 - Mr. Perfect.mp3")
    player.add_to_playlist(r"c:\Users\Harika Yarra\Music\[iSongs.info] 01 - Niluvadhamu Ninu Epudaina.mp3")

    player.play()

    while True:
        choice = input("Enter command (play/pause/resume/stop/next/previous): ").lower()
        if choice == "play":
            player.play()
        elif choice == "pause":
            player.pause()
        elif choice == "resume":
            player.resume()
        elif choice == "stop":
            player.stop()
        elif choice == "next":
            player.next_song()
        elif choice == "previous":
            player.previous_song()
        else:
            print("Invalid command")
p