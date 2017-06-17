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
LED21 = 21
LED22 = 22
LED23 = 23
LED24 = 24
LED25 = 25
LED26 = 26
LED27 = 27

LED10 = 10
LED21 = 20


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

GPIO.setup(LED10, GPIO.OUT)

GPIO.setup(20, GPIO.IN)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию

while True :
 GPIO.output(LED2,True),
 p27 = GPIO.input(27)
 print(p27),
 p26 = GPIO.input(26)
 print(p26),
 p25 = GPIO.input(25)
 print(p25),
 p24 = GPIO.input(24)
 print(p24),
 p23 = GPIO.input(23)
 print(p23),
 p22 = GPIO.input(22)
 print(p22),
 p21 = GPIO.input(21)
 print(p21),
 GPIO.output(LED2,False),
 time.sleep(0.03)
 GPIO.output(LED3,True), 
 p27 = GPIO.input(27)
 print(p27),
 p26 = GPIO.input(26)
 print(p26),
 p25 = GPIO.input(25)
 print(p25),
 p24 = GPIO.input(24)
 print(p24),
 p23 = GPIO.input(23)
 print(p23),
 p22 = GPIO.input(22)
 print(p22),
 p21 = GPIO.input(21)
 print(p21),
 GPIO.output(LED3,False),
 time.sleep(0.03) 
 GPIO.output(LED4,True),
 p27 = GPIO.input(27)
 print(p27),
 p26 = GPIO.input(26)
 print(p26),
 p25 = GPIO.input(25)
 print(p25),
 p24 = GPIO.input(24)
 print(p24),
 p23 = GPIO.input(23)
 print(p23),
 p22 = GPIO.input(22)
 print(p22),
 p21 = GPIO.input(21)
 print(p21)
 GPIO.output(LED4,False),
 time.sleep(0.03) 
 GPIO.output(LED10,True),
# time.sleep(0.03)
 # print('aaa')
# p20 = GPIO.input(20)
# print(p20)
# print('bbb')
# GPIO.output(LED10,False), 
 time.sleep(0.5)
 

