import pygame
import os
import time

ASSETS_DIR = "assets"
AUDIO_FILE = "1.mp3"

def test_audio():
    print(f"Current Working Directory: {os.getcwd()}")
    print("Initializing pygame mixer...")
    try:
        pygame.mixer.init()
    except Exception as e:
        print(f"Error initializing mixer: {e}")
        return

    # Try absolute path based on CWD
    sound_path = os.path.join(os.getcwd(), ASSETS_DIR, AUDIO_FILE)
    print(f"Looking for sound at: {sound_path}")
    
    if not os.path.exists(sound_path):
        print("Error: File not found!")
        # Try finding it relative to script if CWD is wrong
        script_dir = os.path.dirname(os.path.abspath(__file__))
        sound_path = os.path.join(script_dir, ASSETS_DIR, AUDIO_FILE)
        print(f"Retrying with script relative path: {sound_path}")
        if not os.path.exists(sound_path):
            print("Error: File still not found!")
            return

    try:
        print("Loading sound...")
        sound = pygame.mixer.Sound(sound_path)
        print("Playing sound...")
        sound.play()
        
        # Wait for sound to finish
        print("Waiting 5 seconds...")
        time.sleep(5) 
        print("Done.")
    except Exception as e:
        print(f"Error playing sound: {e}")

if __name__ == "__main__":
    test_audio()
