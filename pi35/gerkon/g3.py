#! /usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
#GPIO.setup(8, GPIO.OUT)
#
#GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
#
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
#
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию

while True :

 GPIO.output(2,True),
 time.sleep(0.03)
 print(GPIO.input(27)),
 print(GPIO.input(26)),
 print(GPIO.input(25)),
 print(GPIO.input(24)),
 print(GPIO.input(23)),
 print(GPIO.input(22)),
 GPIO.output(2,False),
 GPIO.output(3,True),
 time.sleep(0.03) 
 print(GPIO.input(27)),
 print(GPIO.input(26)),
 print(GPIO.input(25)),
 print(GPIO.input(24)),
 print(GPIO.input(23)),
 print(GPIO.input(22)),
 GPIO.output(3,False),
 GPIO.output(4,True),
 time.sleep(0.03)
 print(GPIO.input(27)),
 print(GPIO.input(26)),
 print(GPIO.input(25)),
 print(GPIO.input(24)),
 print(GPIO.input(23)),
 print(GPIO.input(22)),
 GPIO.output(4,False),
 GPIO.output(5,True),
 time.sleep(0.03)
 print(GPIO.input(27)),
 print(GPIO.input(26)),
 print(GPIO.input(25)),
 print(GPIO.input(24)),
 print(GPIO.input(23)),
 print(GPIO.input(22)),
 GPIO.output(5,False),
 GPIO.output(6,True),
 time.sleep(0.03)
 print(GPIO.input(27)),
 print(GPIO.input(26)),
 print(GPIO.input(25)),
 print(GPIO.input(24)),
 print(GPIO.input(23)),
 print(GPIO.input(22)),
 GPIO.output(6,False),
 GPIO.output(7,True),
 time.sleep(0.03)
 print(GPIO.input(27)),
 print(GPIO.input(26)),
 print(GPIO.input(25)),
 print(GPIO.input(24)),
 print(GPIO.input(23)),
 print(GPIO.input(22))
 GPIO.output(7,False),
 GPIO.output(10,True),
 time.sleep(0.03) 
 print(GPIO.input(21)),
 print(GPIO.input(20)),
 print(GPIO.input(19)),
 print(GPIO.input(18)),
 print(GPIO.input(17)),
 print(GPIO.input(16)),
 GPIO.output(10,False),
 GPIO.output(11,True),
 time.sleep(0.03)
 print(GPIO.input(21)),
 print(GPIO.input(20)),
 print(GPIO.input(19)),
 print(GPIO.input(18)),
 print(GPIO.input(17)),
 print(GPIO.input(16)),
 GPIO.output(11,False),
 GPIO.output(12,True),
 time.sleep(0.03)
 print(GPIO.input(21)),
 print(GPIO.input(20)),
 print(GPIO.input(19)),
 print(GPIO.input(18)),
 print(GPIO.input(17)),
 print(GPIO.input(16)),
 GPIO.output(12,False)
 GPIO.output(13,True),
 time.sleep(0.03)
 print(GPIO.input(21)),
 print(GPIO.input(20)),
 print(GPIO.input(19)),
 print(GPIO.input(18)),
 print(GPIO.input(17)),
 print(GPIO.input(16)),
 GPIO.output(13,False)
 GPIO.output(14,True),
 time.sleep(0.03)
 print(GPIO.input(21)),
 print(GPIO.input(20)),
 print(GPIO.input(19)),
 print(GPIO.input(18)),
 print(GPIO.input(17)),
 print(GPIO.input(16)),
 GPIO.output(14,False)
 GPIO.output(15,True),
 time.sleep(0.03)
 print(GPIO.input(21)),
 print(GPIO.input(20)),
 print(GPIO.input(19)),
 print(GPIO.input(18)),
 print(GPIO.input(17)),
 print(GPIO.input(16))
 GPIO.output(15,False)
 time.sleep(0.1)
 

