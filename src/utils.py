import os
import pip
from mutagen.mp3 import MP3
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

class MP3Player:
    mixer.init()
    song_playing = False

    # start_at, end_at in ms
    def __init__(self, play_file=None, volume=100, start_at=0, end_at=0):
        self.play_file = play_file
        self.start_at = start_at
        self.volume = volume
        self.end_at = end_at

    def PlayMp3File(self):
        if isinstance(self.play_file, str) == False or self.play_file == None:
            print(TypeError("File path must be instanceof string"))
            return

        if self.play_file.lower().endswith('.mp3'):
            print(TypeError("Filetype of file path must be mp3"))
            return

        if not self.start_at: self.start_at = 0
        if not self.end_at: self.end_at = 0
        
        try:
            mixer.music.load(self.play_file)
        except Exception as e:
            print(Exception(e))
            return

        song_playing = True

        while song_playing:
            if(mixer.Sound.get_length() > MP3(self.play_file).info.length): song_playing = False
            print(mixer.Sound.get_length, ":", MP3(self.play_file).info.length)
    
    def SetVolume(self):
        pass # leave blank for now