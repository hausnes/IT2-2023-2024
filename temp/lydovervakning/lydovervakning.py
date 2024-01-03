import sounddevice as sd
import numpy as np
import pygame
# import keyboard

# Initialize Pygame
pygame.init()

# Initialize the Pygame mixer
pygame.mixer.init()

# Load the mp3 file
pygame.mixer.music.load('alarm-kort.mp3')

# Function to play the alarm sound and print the volume
def audio_callback(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print("Volume:", volume_norm)
    if volume_norm > 100 and not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()

# def quit_program():  # new function
#     pygame.mixer.music.stop()
#     pygame.quit()
#     quit()

# keyboard.add_hotkey('q', quit_program)  # bind 'q' key to quit_program function

with sd.InputStream(callback=audio_callback):
    while True:
        pass  # Do nothing and loop forever


# Attempts to handle quitting using threads
# threading.Thread(target=listen_for_quit).start()
    
# def listen_for_quit():
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.mixer.music.stop()
#                 pygame.quit()
#                 quit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_q:
#                     pygame.mixer.music.stop()
#                     pygame.quit()
#                     quit()