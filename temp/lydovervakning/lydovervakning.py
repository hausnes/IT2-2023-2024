import sounddevice as sd
import numpy as np
import pygame

# Initialize Pygame
pygame.init()

# Initialize the Pygame mixer
pygame.mixer.init()

# Load the mp3 file
pygame.mixer.music.load('alarm-kort.mp3')

def audio_callback(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print("Volume:", volume_norm)
    if volume_norm > 100 and not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()

with sd.InputStream(callback=audio_callback):
    sd.sleep(30000)