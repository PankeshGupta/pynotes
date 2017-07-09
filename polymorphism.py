class AudioFile():
    def endswith(self,filename):
        file_ext = filename.split('.')
        if self.ext == file_ext[1]:
            return True
        else:
            return False
    def __init__(self,filename):
        if not self.endswith(filename):
            raise Exception("Invalid File Format")
        self.filename = filename
class Mp3(AudioFile):
    ext = "mp3"
    def play(self):
        print("playing song {} with mp3 extension ".format(self.filename))

class Wav():
    ext = "wav"
    def play(self):
        
        print("playing {} as wav file".format(self.filename))
class Ogg():
    ext = "ogg"
    def play(self):
        print("playing {} as an ogg file".format(self.filename))
        
if __name__ == "main":
    main()
        
    
