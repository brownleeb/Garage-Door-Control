#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, GPIO.PUD_UP)
GPIO.setwarnings(False)

if GPIO.input(11):
	print '0'
else:
	print '1'

