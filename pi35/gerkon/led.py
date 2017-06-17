#! /usr/bin/env python
# coding: utf-8


import RPi.GPIO as GPIO
import time

#S1 = 'LED'


#for i in range(2, 27):
#    print(i)
#   print((S1 + str(i)) + "=" + int(i))

#   (S1 + str(i)) = str(i)



#   print b

#LED = 2
#LED3 = 3
#LED4 = 4
#LED5 = 5
#LED6 = 6
#LED7 = 7
#LED8 = 8
#LED9 = 9

LED2 = 2
LED3 = 3
LED4 = 4
LED5 = 5
LED6 = 6
LED7 = 7
LED8 = 8
LED9 = 9
LED10 = 10
LED11 = 11
LED12 = 12
LED13 = 13
LED14 = 14
LED15 = 15
LED16 = 16
LED17 = 17
LED18 = 18
LED19 = 19
LED20 = 20
LED21 = 21
LED22 = 22
LED23 = 23
LED24 = 24
LED25 = 25
LED26 = 26
LED26 = 27




GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
GPIO.setup(LED5, GPIO.OUT)
GPIO.setup(LED6, GPIO.OUT)
GPIO.setup(LED7, GPIO.OUT)
GPIO.setup(LED8, GPIO.OUT)
GPIO.setup(LED9, GPIO.OUT)


while(1):
        GPIO.output(LED2,True)
        time.sleep(0.25)
        GPIO.output(LED2,False)
        time.sleep(0.25)
        GPIO.output(LED3,True)
        time.sleep(0.25)
        GPIO.output(LED3,False)
        time.sleep(0.25)
        GPIO.output(LED4,True)
        time.sleep(0.25)
        GPIO.output(LED4,False)
        time.sleep(0.25)
        GPIO.output(LED5,True)
        time.sleep(0.25)
        GPIO.output(LED5,False)
        time.sleep(0.25)
        GPIO.output(LED6,True)
        time.sleep(0.25)
        GPIO.output(LED6,False)
        time.sleep(0.25)
        GPIO.output(LED7,True)
        time.sleep(0.25)
        GPIO.output(LED7,False)
        time.sleep(0.25)
        GPIO.output(LED8,True)
        time.sleep(0.25)
        GPIO.output(LED8,False)
        time.sleep(0.25)
        GPIO.output(LED9,True)
        time.sleep(0.25)
        GPIO.output(LED9,False)
        time.sleep(0.25)

