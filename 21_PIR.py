#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

PIR_OUT_PIN = 11    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(PIR_OUT_PIN, GPIO.IN)    # Set BtnPin's mode is input

def loop():
	while True:
		if GPIO.input(PIR_OUT_PIN) == GPIO.LOW:
			print '...Movement not detected!'
		else:
			print 'Movement detected!...'

def destroy():
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

