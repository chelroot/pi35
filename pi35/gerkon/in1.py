#! /usr/bin/env python
# coding: utf-8


import RPi.GPIO as GPIO
import time

LED21 = 21
LED22 = 22
LED23 = 23
LED24 = 24
LED25 = 25
LED26 = 26
LED27 = 27


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(27, GPIO.IN)


GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию

pinstate = GPIO.input(27)
print(pinstate),

pinstate = GPIO.input(26)
print(pinstate),

pinstate = GPIO.input(25)
print(pinstate),

pinstate = GPIO.input(24)
print(pinstate),

pinstate = GPIO.input(23)
print(pinstate),

pinstate = GPIO.input(22)
print(pinstate),

pinstate = GPIO.input(21)
print(pinstate),
