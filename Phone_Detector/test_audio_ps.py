import subprocess
import os
import time

ASSETS_DIR = "assets"
AUDIO_FILE = "1.mp3"

def play_sound_powershell(file_path):
    # PowerShell command to play audio
    # explicitly load presentation core for MediaPlayer
    ps_command = f"""
    Add-Type -AssemblyName PresentationCore
    $player = New-Object System.Windows.Media.MediaPlayer
    $player.Open('{file_path}')
    $player.Play()
    Start-Sleep -Seconds 5
    """
    
    cmd = ["powershell", "-c", ps_command]
    
    print(f"Playing {file_path} using PowerShell...")
    try:
        subprocess.run(cmd, check=True)
        print("Playback finished.")
    except subprocess.CalledProcessError as e:
        print(f"Error playing sound: {e}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sound_path = os.path.join(script_dir, ASSETS_DIR, AUDIO_FILE)
    
    if os.path.exists(sound_path):
        play_sound_powershell(sound_path)
    else:
        print(f"File not found: {sound_path}")

if __name__ == "__main__":
    main()
