#! /usr/bin/env python
# coding: utf-8


import RPi.GPIO as GPIO
import time

LED2 = 2
LED3 = 3
LED4 = 4
LED5 = 5
LED6 = 6
LED7 = 7
LED8 = 8
LED9 = 9


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
GPIO.setup(LED5, GPIO.OUT)
GPIO.setup(LED6, GPIO.OUT)
GPIO.setup(LED7, GPIO.OUT)
GPIO.setup(LED8, GPIO.OUT)
GPIO.setup(LED9, GPIO.OUT)


GPIO.output(LED2,True)
GPIO.output(LED3,True)
GPIO.output(LED4,True)
GPIO.output(LED5,True)
GPIO.output(LED6,True)
GPIO.output(LED7,True)
GPIO.output(LED8,True)
GPIO.output(LED9,True)
