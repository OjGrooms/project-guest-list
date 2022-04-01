from playbackTest import playaudio
import RPi.GPIO as GPIO

def button_callback(channel):
    playaudio

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(10, GPIO.RISING,callback=button_callback)

message = input("Press enter to quit\n\n")
GPIO.cleanup

