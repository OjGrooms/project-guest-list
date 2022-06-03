## Generates a time stamp and joins it to the base filename
import datetime
from time import sleep
def fileNameGen():
  for ii in range (10 ):
    basename = "voicerec.wav"
    prefix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    fullname = "_".join([prefix, basename])
    print(fullname)
    return fullname
