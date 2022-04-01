from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_file('/home/joe/Documents/project-guest-list/tests/test.wav')
print('testing audio output')
play(song)