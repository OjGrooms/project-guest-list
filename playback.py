from pydub import AudioSegment
from pydub.playback import play

def playPreamble(): 
  song = AudioSegment.from_file('plamatf.wav')
  play(song)