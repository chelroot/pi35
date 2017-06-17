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

t = 0.09

bb11 = 1
bb12 = 1
bb13 = 1
bb14 = 1
bb15 = 1
bb16 = 1

bb21 = 1
bb22 = 1
bb23 = 1
bb24 = 1
bb25 = 1
bb26 = 1

bb31 = 1
bb32 = 1
bb33 = 1
bb34 = 1
bb35 = 1
bb36 = 1

bb41 = 1
bb42 = 1
bb43 = 1
bb44 = 1
bb45 = 1
bb46 = 1

bb51 = 1
bb52 = 1
bb53 = 1
bb54 = 1
bb55 = 1
bb56 = 1

bb61 = 1
bb62 = 1
bb63 = 1
bb64 = 1
bb65 = 1
bb66 = 1


pwd1 = "/var/www/html/11/a2.html"
a2 = open(pwd1, 'a')



while True :
 now = datetime.now()
 GPIO.output(7,True),
 time.sleep(t)

 if (GPIO.input(27)) == 0:
   if bb11 == 1:
    print('11' + '  off  ' + str(now) + '\n')
   bb11 = 0
 if (GPIO.input(27)) == 1:
   if bb11 == 0:
    print('11' + '  on  ' + str(now) + '\n')
   bb11 = 1
#
 if (GPIO.input(26)) == 0:
    print('12'),
 if (GPIO.input(26)) == 1:
    print('. '), 
 if (GPIO.input(25)) == 0:
    print('13'),
 if (GPIO.input(25)) == 1:
    print('. '),
 if (GPIO.input(24)) == 0:
    print('14'),
 if (GPIO.input(24)) == 1:
    print('. '),
 if (GPIO.input(23)) == 0:
    print('15'),
 if (GPIO.input(23)) == 1:
    print('. '),
 if (GPIO.input(22)) == 0:
    print('16'),
 if (GPIO.input(22)) == 1:
    print('. '),

 GPIO.output(7,False),
 GPIO.output(6,True),
 time.sleep(t) 

 if (GPIO.input(27)) == 0:
    print('21'),
 if (GPIO.input(27)) == 1:
    print('. '),
 if (GPIO.input(26)) == 0:
    print('22'),
 if (GPIO.input(26)) == 1:
    print('. '),
 if (GPIO.input(25)) == 0:
    print('23'),
 if (GPIO.input(25)) == 1:
    print('. '),
 if (GPIO.input(24)) == 0:
    print('24'),
 if (GPIO.input(24)) == 1:
    print('. '),
 if (GPIO.input(23)) == 0:
    print('25'),
 if (GPIO.input(23)) == 1:
    print('. '),
 if (GPIO.input(22)) == 0:
    print('26'),
 if (GPIO.input(22)) == 1:
    print('. '),

 GPIO.output(6,False),
 GPIO.output(5,True),
 time.sleep(t)

 if (GPIO.input(27)) == 0:
    print('31'),
 if (GPIO.input(27)) == 1:
    print('. '),
 if (GPIO.input(26)) == 0:
    print('32'),
 if (GPIO.input(26)) == 1:
    print('. '),
 if (GPIO.input(25)) == 0:
    print('33'),
 if (GPIO.input(25)) == 1:
    print('. '),
 if (GPIO.input(24)) == 0:
    print('34'),
 if (GPIO.input(24)) == 1:
    print('. '),
 if (GPIO.input(23)) == 0:
    print('35'),
 if (GPIO.input(23)) == 1:
    print('. '),
 if (GPIO.input(22)) == 0:
    print('36'),
 if (GPIO.input(22)) == 1:
    print('. '),

 GPIO.output(5,False),
 GPIO.output(4,True),
 time.sleep(t)

 if (GPIO.input(27)) == 0:
    print('41'),
 if (GPIO.input(27)) == 1:
    print('. '),
 if (GPIO.input(26)) == 0:
    print('42'),
 if (GPIO.input(26)) == 1:
    print('. '),
 if (GPIO.input(25)) == 0:
    print('43'),
 if (GPIO.input(25)) == 1:
    print('. '),
 if (GPIO.input(24)) == 0:
    print('44'),
 if (GPIO.input(24)) == 1:
    print('. '),
 if (GPIO.input(23)) == 0:
    print('45'),
 if (GPIO.input(23)) == 1:
    print('. '),
 if (GPIO.input(22)) == 0:
    print('46'),
 if (GPIO.input(22)) == 1:
    print('. '),

 GPIO.output(4,False),
 GPIO.output(3,True),
 time.sleep(t)
 
 if (GPIO.input(27)) == 0:
    print('51'),
 if (GPIO.input(27)) == 1:
    print('. '),
 if (GPIO.input(26)) == 0:
    print('52'),
 if (GPIO.input(26)) == 1:
    print('. '),
 if (GPIO.input(25)) == 0:
    print('53'),
 if (GPIO.input(25)) == 1:
    print('. '),
#
 if (GPIO.input(24)) == 0:
   if bb54 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '54' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb54 = 0
 if (GPIO.input(24)) == 1:
   if bb54 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '54' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb54 = 1
#
 if (GPIO.input(23)) == 0:
   if bb55 == 1:
    print('55' + '  off  ' + str(now) + '\n')
   bb55 = 0
 if (GPIO.input(23)) == 1:
   if bb55 == 0:
    print('55' + '  on  ' + str(now) + '\n')
   bb55 = 1
#
 if (GPIO.input(22)) == 0:
   if bb56 == 1:
    print('56' + '  off  ' + str(now) + '\n')
   bb56 = 0

 if (GPIO.input(22)) == 1:
   if bb56 == 0:
    print('56' + '  on  ' + str(now) + '\n')
   bb56 = 1


 GPIO.output(3,False),
 GPIO.output(2,True),
 time.sleep(t)

 if (GPIO.input(27)) == 0:
    print('61'),
 if (GPIO.input(27)) == 1:
    print('. '),
 if (GPIO.input(26)) == 0:
    print('62'),
 if (GPIO.input(26)) == 1:
    print('. '),
 if (GPIO.input(25)) == 0:
    print('63'),
 if (GPIO.input(25)) == 1:
    print('. '),
 if (GPIO.input(24)) == 0:
    print('64'),
 if (GPIO.input(24)) == 1:
    print('. '),
 if (GPIO.input(23)) == 0:
    print('65'),
 if (GPIO.input(23)) == 1:
    print('. '),
 if (GPIO.input(22)) == 0:
    print('66')
 if (GPIO.input(22)) == 1:
    print('. ')
 GPIO.output(2,False),

















