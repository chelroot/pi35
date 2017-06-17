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
GPIO.setup(8, GPIO.OUT)
#
GPIO.setup(9, GPIO.OUT)
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

t = 0.05

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

#aa34 = 1

pwd1 = "/var/www/html/a2.html"
pwd2 = "/var/www/html/aa2.html"

a2 = open(pwd1, 'a')
aa2 = open(pwd2, 'a')

g1 = 7
g2 = 6
g3 = 5
g4 = 4
g5 = 3
g6 = 2
dd71 = 1

while True :
 for nn in 7, 6, 5, 4, 3, 2:
  gg = ('g%s' % nn)
#  print(gg)
  now = datetime.now()
  GPIO.output(nn,True),
  time.sleep(t)
  da = ('dd%s' % nn + '1')
#  print(da)
  if (GPIO.input(27)) == 0:
    if dd71 == 1:
     a2.write('<br />' + gg +'1' + '  off ' + str(now) + '\n'),
    dd71 = 0
  else:
    if dd71 == 0:
     a2.write('<br />' + gg +'1' + '  on  ' + str(now) + '\n'),
    dd71 = 0
  print(dd71)




  if (GPIO.input(26)) == 0:
    if bb12 == 1:
     a2.write('<br />' + '12' + '  off ' + str(now) + '\n'),
    bb12 = 0
  else:
    if bb12 == 0:
     a2.write('<br />' + '12' + '  on  ' + str(now) + '\n'),
    bb12 = 1
  if (GPIO.input(25)) == 0:
    if bb13 == 1:
     a2.write('<br />' + '13' + '  off ' + str(now) + '\n'),
    bb13 = 0
  if (GPIO.input(25)) == 1:
    if bb13 == 0:
     a2.write('<br />' + '13' + '  on  ' + str(now) + '\n'),
    bb13 = 1
  if (GPIO.input(24)) == 0:
    if bb14 == 1:
     a2.write('<br />' + '14' + '  off ' + str(now) + '\n'),
    bb14 = 0
  if (GPIO.input(24)) == 1:
    if bb14 == 0:
     a2.write('<br />' + '14' + '  on  ' + str(now) + '\n'),
    bb14 = 1
  if (GPIO.input(23)) == 0:
    if bb15 == 1:
     a2.write('<br />' + '15' + '  off ' + str(now) + '\n'),
    bb15 = 0
  if (GPIO.input(23)) == 1:
    if bb15 == 0:
     a2.write('<br />' + '15' + '  on  ' + str(now) + '\n'),
    bb15 = 1
  if (GPIO.input(22)) == 0:
    if bb16 == 1:
     a2.write('<br />' + '16' + '  off ' + str(now) + '\n'),
    bb16 = 0
  if (GPIO.input(22)) == 1:
    if bb16 == 0:
     a2.write('<br />' + '16' + '  on  ' + str(now) + '\n'),
    bb16 = 1

  GPIO.output(nn,False),
















