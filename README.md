# Project Guestlist

This project is built to run on raspberryPi on rasberryPi 3B+. It is designed to interface with
a disemboweled rotory phone, where the handset is terminated into retrofit mono 3.5mm audio jack
and connected to a headphone/mic usb adapter, the receiver switch is interfaced with a GPIO 3.3v pin
and a I/O pin to detect when the handset is lifted, and the rotor dial is not connected to anything.

This project can be expaned on to utilize the rotor for other purposes, but this specific application
is as follows:

1. Let a user lift the handset off the rest and wait 2 seconds (to put the speaker to their ear)
2. Play a brief message instructing the user to leave a message
3. Record the message from the user until the handset is returned to the receiver

After the message is recorded, it will be saved to the audio folder with a timestamped title.
