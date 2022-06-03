import RPi.GPIO as gpio
from recorder import Recorder
from filename import *
from playback import *
from timer import ButtonTimeout
gpio.setmode(gpio.BOARD)

class ButtonRecorder(object):
    def __init__(self):
        self.filename = fileNameGen()
        gpio.setup(16, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        self.rtc = ButtonTimeout(120, self.falling) ## ButtonTimeout(secondsToTime, callbackFunction)
        self.recorder = Recorder(channels=2)

    def start(self):
        gpio.add_event_detect(16, gpio.RISING, callback=self.rising, bouncetime=50)

    def falling(self, channel=16):
        print('returned to rest')
        gpio.remove_event_detect(channel)
        gpio.add_event_detect(channel, gpio.RISING, callback=self.rising, bouncetime=50)
        self.rtc.cancel()
        self.recfile.stop_recording()
        self.recfile.close()

    def rising(self, channel=16):
        print('lifted from rest')
        gpio.remove_event_detect(channel)
        gpio.add_event_detect(channel, gpio.FALLING, callback=self.falling, bouncetime=50)
        sleep(1)
        playPreamble()
        self.rtc.start()
        self.recfile = self.recorder.open(self.filename, 'wb')
        self.recfile.start_recording()

rec = ButtonRecorder()
rec.start()

try:
    print('Ready, trying input')
    input()

except KeyboardInterrupt:
    pass

gpio.cleanup()