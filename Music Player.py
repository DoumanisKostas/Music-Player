import pygame
import os
from tkinter import filedialog
import tkinter as tk
import random

# Initialize Pygame
pygame.init()

# Create Tkinter root window
root = tk.Tk()
root.withdraw()

# Set up display
WIDTH, HEIGHT = 870, 520
FPS = 60

# Colors
WHITE = (255, 255, 255)

# Create Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# Fonts
font = pygame.font.Font(None, 36)

# Load images
background_image = pygame.image.load("music_note_background.jpg")

# Function to get a list of supported music file extensions
def get_supported_extensions():
    return [".mp3", ".wav", ".ogg", ".flac"]

# Function to load a song
def load_song():
    file_paths = filedialog.askopenfilenames(initialdir="/", title="Select Song",
                                             filetypes=[("Music Files", get_supported_extensions())])
    return list(file_paths)

# Function to play a song
def play_song(song_path):
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

# Function to stop playing the current song
def stop_song():
    pygame.mixer.music.stop()

# Function to pause or resume the current song
def pause_resume_song():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

# Function to display text on the screen
def display_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

# Main function
def main():
    clock = pygame.time.Clock()

    playing_songs = []
    current_song_index = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Press 'S' to stop the current song
                    stop_song()
                elif event.key == pygame.K_p:  # Press 'P' to pause or resume the current song
                    pause_resume_song()
                elif event.key == pygame.K_n:  # Press 'N' to go to the next song
                    current_song_index = (current_song_index + 1) % len(playing_songs)
                    play_song(playing_songs[current_song_index])
                elif event.key == pygame.K_b:  # Press 'B' to go to the previous song
                    current_song_index = (current_song_index - 1) % len(playing_songs)
                    play_song(playing_songs[current_song_index])

        screen.blit(background_image, (0, 0))  # Music note background

        display_text("Music Player", 10, 10)
        display_text("Press 'O' to Open a File", 10, 50)

        if playing_songs:
            display_text(f"Now Playing: {os.path.basename(playing_songs[current_song_index])}", 10, 100)

        pygame.display.update()
        clock.tick(FPS)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_o]:  # Press 'O' to open files
            song_paths = load_song()
            if song_paths:
                playing_songs = song_paths
                current_song_index = 0
                play_song(playing_songs[current_song_index])

if __name__ == "__main__":
    main()
