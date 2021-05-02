import os
import pip
import time
from mutagen.mp3 import MP3
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

class MP3Player:
    def __init__(self, play_file=None, volume=100, start_at=0):
        mixer.init()
        self.play_file = play_file
        self.start_at = start_at # [wip]
        self.volume = volume

    def PlayMp3File(self):
        if isinstance(self.play_file, str) == False or self.play_file == None:
            print(TypeError("File path must be instanceof string"))
            return

        if not self.play_file.lower().endswith('.mp3'):
            print(TypeError("Filetype of file path must be mp3"))
            return None

        if self.volume > 100 or self.volume < 100:
            print(TypeError("Volume must be no greater than 100 or less than 100"))
            return

        if not self.start_at:
            self.start_at = 0
        
        try:
            _volume = self.volume / 100
            mixer.music.load(self.play_file)
            mixer.music.set_volume(_volume)
            mixer.music.play()
        except Exception as e:
            print(Exception(e))
            return

        while True:
            print("Now playing " + self.play_file + " on volume " + str(self.volume))
            print("Press 'p' to pause, 'r' to resume, 'e' to quit")
            
            query = input()
            if query.lower() == 'p':
                mixer.music.pause()

            elif query.lower() == 'r':
                mixer.music.unpause()

            elif query.lower() == 'e':
                mixer.music.stop()
                break

            else:
                print("That command does not exist.")
                time.sleep(1)

            os.system('cls' if os.name == 'nt' else 'clear')