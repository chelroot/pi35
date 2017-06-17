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

t = 0.03

while True :
 now = datetime.now()
 GPIO.output(7,True),
 time.sleep(t)

 if (GPIO.input(27)) == 0:
    print('11'),
 if (GPIO.input(27)) == 1:
    print('. '),
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
 if (GPIO.input(24)) == 0:
    print('54'),
 if (GPIO.input(24)) == 1:
    print('. '),
 if (GPIO.input(23)) == 0:
    print('55'),
 if (GPIO.input(23)) == 1:
    print('. '),
 if (GPIO.input(22)) == 0:
    print('56'),
 if (GPIO.input(22)) == 1:
    print('. '),

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

















