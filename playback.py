from pydub import AudioSegment
from pydub.playback import play

def playPreamble(): 
  # "Hello, please leave a message after the tone"
  song = AudioSegment.from_file('plamatf.wav')
  play(song)