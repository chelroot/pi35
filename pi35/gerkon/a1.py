#! /usr/bin/env python
# coding: utf-8


import RPi.GPIO as GPIO
import time

LED = 21
LED = 22
LED = 23
LED = 24
LED = 25
LED = 26
LED = 27


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setup(LED, GPIO.OUT)
GPIO.setup(21, GPIO.IN)
#GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # подтяжка к земле

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию


pinstate = GPIO.input(21)

print(pinstate),
