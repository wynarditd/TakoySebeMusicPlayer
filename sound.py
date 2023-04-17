import pygame

from mutagen import mp3, oggopus, wave



class MusicPlayer():
    def __init__(self):
        pygame.init()
        self.paused = False
        self.length = None
        self.music_path = ""

    def play(self, path):
        try:
            pygame.mixer.music.stop()
        except:
            pass
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)
        try:
            self.length = pygame.mixer.Sound(path).get_length()
        except:
            pass
        self.music_path = path


    def pause(self):
        self.paused = not self.paused
        if self.paused:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        
    def stop(self):
        pygame.mixer.music.stop()

    def sound_length(self):
        return int(pygame.mixer.Sound(self.music_path).get_length())
    
    def startWith(self, time):
        try:
            pygame.mixer.music.load(self.music_path)
            pygame.mixer.music.play(-1,start=time)
        except:
            pass
        

    #def start_from(self):
    #    pygame.mixer.music.load(self.music_path)
    #    pygame.mixer.music.play(-1,start=)