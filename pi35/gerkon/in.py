#! /usr/bin/env python
# coding: utf-8


import RPi.GPIO as GPIO
import time

LED = 2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setup(LED, GPIO.OUT)
GPIO.setup(2, GPIO.IN)
#GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # подтяжка к земле

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию


pinstate = GPIO.input(2)

print(pinstate),
