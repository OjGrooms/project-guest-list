import RPi.GPIO as gpio
from recorder import Recorder
from filename import *
from playback import *
from timer import ButtonTimeout
gpio.setmode(gpio.BOARD)

class ButtonRecorder(object):
    def __init__(self):
        # Setting up the button to be used as an input.cd 
        gpio.setup(18, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        gpio.setup(16, gpio.IN, pull_up_down=gpio.PUD_DOWN)
        # Creating a timer that will call the falling function after 120 seconds.
        self.rtc = ButtonTimeout(15, self.handle_timer)
        # Creating a Recorder object with 2 channels.
        self.recorder = Recorder(channels=2)
        self.timerFired = False
        self.handsetLowered = False

    def start(self):
        gpio.add_event_detect(18, gpio.RISING, callback=self.handset_up, bouncetime=50)

    def handset_up(self, channel=18):
        """
        The handset_up function is called when the handset is lifted from the rest. It starts the real
        time clock, sets the handsetLowered variable to False, sets the timerFired variable to False,
        removes the event detection on the channel, adds event detection on the channel, and starts
        recording
        
        :param channel: the GPIO pin number that the handset is connected to, defaults to 18 (optional)
        """
        print('lifted from rest')
        self.rtc.start()
        self.handsetLowered = False
        self.timerFired = False
        gpio.remove_event_detect(channel)
        gpio.add_event_detect(16, gpio.RISING, callback=self.handset_down, bouncetime=50)
        self.start_recording()


    def handset_down(self, channel=16):
        """
        The handset_down function is called when the handset is returned to the rest position. It sets
        the handsetLowered variable to True, and if the timerFired variable is False, it stops recording
        
        :param channel: The GPIO pin number that the handset is connected to, defaults to 16 (optional)
        """
        print('returned to rest')
        self.handsetLowered = True
        if self.timerFired == False:
            self.stop_recording()
            next
        gpio.remove_event_detect(channel)
        gpio.add_event_detect(18, gpio.RISING, callback=self.handset_up, bouncetime=50)
    
    def handle_timer(self):
        """
        If the handset is not lowered, stop recording
        """
        print('Timer fired')
        self.timerFired = True
        self.rtc.cancel()
        if self.handsetLowered == False:
            self.stop_recording()

    def stop_recording(self):
        """
        It stops the recording, closes the file, and cancels the timer
        """
        self.recfile.stop_recording()
        self.recfile.close()
        self.rtc.cancel()

    def start_recording(self):
        """
        It starts after a 1 second delay, plays a preamble, and then starts recording
        """
        sleep(1)
        playPreamble()
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