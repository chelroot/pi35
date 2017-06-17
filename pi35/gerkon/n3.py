#! /usr/bin/env python
# coding: utf-8

import RPi.GPIO as GPIO
import time, os
from datetime import datetime

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

bb2 = 0
bb22 = 0


pwd1 = "/var/www/html/a2.html"
a2 = open(pwd1, 'a')

while True :
 now = datetime.now()
 GPIO.output(2,True),
 time.sleep(0.33)
# print(GPIO.input(27)),
 if (GPIO.input(27)) == 0:
   if bb2 == 1:
    print('02' + '  off  ' + str(now) + '\n')
   bb2 = 0

 if (GPIO.input(27)) == 1:
   if bb2 == 0:
    print('02' + '  on  ' + str(now) + '\n')
   bb2 = 1


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
 
 if (GPIO.input(22)) == 0:
   if bb22 == 1:
    print('22' + '  off  ' + str(now) + '\n')
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '01' + '  on  ' + str(now) + '\n'),
    a2.close()

   bb22 = 0

 if (GPIO.input(22)) == 1:
   if bb22 == 0:
    print('22' + '  on  ' + str(now) + '\n')
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '01' + '  on  ' + str(now) + '\n'),
    a2.close()
    

   bb22 = 1



 GPIO.output(7,False),
 

