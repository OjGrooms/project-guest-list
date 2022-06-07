import RPi.GPIO as gpio
from recorder import Recorder
from filename import *
from playback import *
from timer import ButtonTimeout
gpio.setmode(gpio.BOARD)

class ButtonRecorder(object):
    def __init__(self):
        # Setting up the button to be used as an input.
        gpio.setup(18, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        # Creating a timer that will call the falling function after 120 seconds.
        self.rtc = ButtonTimeout(5, self.falling)
        # Creating a Recorder object with 2 channels.
        self.recorder = Recorder(channels=2)

    def start(self):
        gpio.add_event_detect(18, gpio.RISING, callback=self.rising, bouncetime=50)

    def falling(self, channel=18):
        """
        The falling function is called when the button is released. It removes the event detection for
        the falling edge and adds it for the rising edge. It also stops the recording and closes the
        file
        
        :param channel: The GPIO pin number that the button is connected to, defaults to 18 (optional)
        """
        print('returned to rest')
        gpio.remove_event_detect(channel)
        gpio.add_event_detect(channel, gpio.RISING, callback=self.rising, bouncetime=50)
        self.rtc.cancel()
        self.recfile.stop_recording()
        self.recfile.close()

    def rising(self, channel=18):
        """
        The rising function is called when the button is pressed, and it starts the recording process
        
        :param channel: The GPIO pin number that the button is connected to, defaults to 18 (optional)
        """
        print('lifted from rest')
        gpio.remove_event_detect(channel)
        gpio.add_event_detect(channel, gpio.FALLING, callback=self.falling, bouncetime=50)
        sleep(1)
        playPreamble()
        self.rtc.start()
        self.recfile = self.recorder.open(fileNameGen(), 'wb')
        self.recfile.start_recording()

rec = ButtonRecorder()
rec.start()

try:
    print('Ready, trying input')
    input()

except KeyboardInterrupt:
    pass

gpio.cleanup()