#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
#Pin 15 on RPi GPIO header is GPIO1 (Relay)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.cleanup()
