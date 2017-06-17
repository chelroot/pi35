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


pwd1 = "/var/www/html/a2.html"
pwd2 = "/var/www/html/aa2.html"
d11 = "/var/www/html/d11.html"
d12 = "/var/www/html/d12.html"
d21 = "/var/www/html/d21.html"
d22 = "/var/www/html/d22.html"
d23 = "/var/www/html/d23.html"
d31 = "/var/www/html/d31.html"
d32 = "/var/www/html/d32.html"
d33 = "/var/www/html/d33.html"


a2 = open(pwd1, 'a')
aa2 = open(pwd2, 'a')
a11 = open(d11, 'a')
a12 = open(d12, 'a')
a21 = open(d21, 'a')
a22 = open(d22, 'a')
a23 = open(d23, 'a')
a31 = open(d31, 'a')
a32 = open(d32, 'a')
a33 = open(d33, 'a')


while True :
 now = datetime.now()
 GPIO.output(7,True),
 time.sleep(t)

 if (GPIO.input(27)) == 0:
   if bb11 == 1:
    a11 = open(d11, 'a')
    a11.write('<br />' + '11' + '  off  ' + str(now) + '\n'),
    a11.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '11' + '  off  ' + str(now) + '\n'),
    a2.close()

   bb11 = 0
 if (GPIO.input(27)) == 1:
   if bb11 == 0:
    a11 = open(d11, 'a')
    a11.write('<br />' + '11' + '  on  ' + str(now) + '\n'),
    a11.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '11' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb11 = 1
#
 if (GPIO.input(26)) == 0:
   if bb12 == 1:
    a12 = open(d12, 'a')
    a12.write('<br />' + '12' + '  off  ' + str(now) + '\n'),
    a12.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '12' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb12 = 0
 if (GPIO.input(26)) == 1:
   if bb12 == 0:
    a12 = open(d12, 'a')
    a12.write('<br />' + '12' + '  on  ' + str(now) + '\n'),
    a12.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '12' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb12 = 1
#
 if (GPIO.input(25)) == 0:
   if bb13 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '13' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb13 = 0
 if (GPIO.input(25)) == 1:
   if bb13 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '13' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb13 = 1
#
 if (GPIO.input(24)) == 0:
   if bb14 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '14' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb14 = 0
 if (GPIO.input(24)) == 1:
   if bb14 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '14' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb14 = 1
#
 if (GPIO.input(23)) == 0:
   if bb15 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '15' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb15 = 0
 if (GPIO.input(23)) == 1:
   if bb15 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '15' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb15 = 1
#
 if (GPIO.input(22)) == 0:
   if bb16 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '16' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb16 = 0
 if (GPIO.input(22)) == 1:
   if bb16 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '56' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb16 = 1

 GPIO.output(7,False),
 GPIO.output(6,True),
 time.sleep(t) 

 if (GPIO.input(27)) == 0:
   if bb21 == 1:
    a21 = open(d21, 'a')
    a21.write('<br />' + '21' + '  off  ' + str(now) + '\n'),
    a21.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '21' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb21 = 0
 if (GPIO.input(27)) == 1:
   if bb21 == 0:
    a21 = open(d21, 'a')
    a21.write('<br />' + '21' + '  on  ' + str(now) + '\n'),
    a21.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '21' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb21 = 1
#
 if (GPIO.input(26)) == 0:
   if bb22 == 1:
    a22 = open(d22, 'a')
    a22.write('<br />' + '22' + '  off  ' + str(now) + '\n'),
    a22.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '22' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb22 = 0
 if (GPIO.input(26)) == 1:
   if bb22 == 0:
    a22 = open(d22, 'a')
    a22.write('<br />' + '22' + '  on  ' + str(now) + '\n'),
    a22.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '22' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb22 = 1
#
 if (GPIO.input(25)) == 0:
   if bb23 == 1:
    a23 = open(d23, 'a')
    a23.write('<br />' + '23' + '  off  ' + str(now) + '\n'),
    a23.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '23' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb23 = 0
 if (GPIO.input(25)) == 1:
   if bb23 == 0:
    a23 = open(d23, 'a')
    a23.write('<br />' + '23' + '  on  ' + str(now) + '\n'),
    a23.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '23' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb23 = 1
#
 if (GPIO.input(24)) == 0:
   if bb24 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '24' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb24 = 0
 if (GPIO.input(24)) == 1:
   if bb24 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '24' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb24 = 1
#
 if (GPIO.input(23)) == 0:
   if bb25 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '25' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb25 = 0
 if (GPIO.input(23)) == 1:
   if bb25 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '25' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb25 = 1
#
 if (GPIO.input(22)) == 0:
   if bb26 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '26' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb26 = 0
 if (GPIO.input(22)) == 1:
   if bb26 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '26' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb26 = 1

 GPIO.output(6,False),
 GPIO.output(5,True),
 time.sleep(t)


 if (GPIO.input(27)) == 0:
   if bb31 == 1:
    a31 = open(d31, 'a')
    a31.write('<br />' + '31' + '  off  ' + str(now) + '\n'),
    a31.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '31' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb31 = 0
 if (GPIO.input(27)) == 1:
   if bb31 == 0:
    a31 = open(d31, 'a')
    a31.write('<br />' + '31' + '  on  ' + str(now) + '\n'),
    a31.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '31' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb31 = 1
#
 if (GPIO.input(26)) == 0:
   if bb32 == 1:
    a32 = open(d32, 'a')
    a32.write('<br />' + '32' + '  off  ' + str(now) + '\n'),
    a32.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '32' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb32 = 0
 if (GPIO.input(26)) == 1:
   if bb32 == 0:
    a32 = open(d32, 'a')
    a32.write('<br />' + '32' + '  on  ' + str(now) + '\n'),
    a32.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '32' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb32 = 1
#
 if (GPIO.input(25)) == 0:
   if bb33 == 1:
    a33 = open(d33, 'a')
    a33.write('<br />' + '33' + '  off  ' + str(now) + '\n'),
    a33.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '33' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb33 = 0
 if (GPIO.input(25)) == 1:
   if bb33 == 0:
    a33 = open(d33, 'a')
    a33.write('<br />' + '33' + '  on  ' + str(now) + '\n'),
    a33.close()
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '33' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb33 = 1
#
 if (GPIO.input(24)) == 0:
   if bb34 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '34' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb34 = 0
 if (GPIO.input(24)) == 1:
   if bb34 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '34' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb34 = 1
#
 if (GPIO.input(23)) == 0:
   if bb35 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '35' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb35 = 0
 if (GPIO.input(23)) == 1:
   if bb35 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '35' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb35 = 1
#
 if (GPIO.input(22)) == 0:
   if bb36 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '36' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb36 = 0
 if (GPIO.input(22)) == 1:
   if bb36 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '36' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb36 = 1

 GPIO.output(5,False),
 GPIO.output(4,True),
 time.sleep(t)

 if (GPIO.input(27)) == 0:
   if bb41 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '41' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb41 = 0
 if (GPIO.input(27)) == 1:
   if bb41 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '41' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb41 = 1
#
 if (GPIO.input(26)) == 0:
   if bb42 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '42' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb42 = 0
 if (GPIO.input(26)) == 1:
   if bb42 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '42' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb42 = 1
#
 if (GPIO.input(25)) == 0:
   if bb43 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '43' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb43 = 0
 if (GPIO.input(25)) == 1:
   if bb53 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '43' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb43 = 1
#
 if (GPIO.input(24)) == 0:
   if bb44 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '44' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb44 = 0
 if (GPIO.input(24)) == 1:
   if bb44 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '44' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb44 = 1
#
 if (GPIO.input(23)) == 0:
   if bb45 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '45' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb45 = 0
 if (GPIO.input(23)) == 1:
   if bb45 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '45' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb45 = 1
#
 if (GPIO.input(22)) == 0:
   if bb46 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '46' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb46 = 0
 if (GPIO.input(22)) == 1:
   if bb46 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '46' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb46 = 1

 GPIO.output(4,False),
 GPIO.output(3,True),
 time.sleep(t)
#
 if (GPIO.input(27)) == 0:
   if bb51 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '51' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb51 = 0
 if (GPIO.input(27)) == 1:
   if bb51 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '51' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb51 = 1
#
 if (GPIO.input(26)) == 0:
   if bb52 == 1:
    aa2 = open(pwd2, 'a')
    aa2.write('<br />' + '52' + '  off  ' + str(now) + '\n'),
    aa2.close()
   bb52 = 0
 if (GPIO.input(26)) == 1:
   if bb52 == 0:
    aa2 = open(pwd2, 'a')
    aa2.write('<br />' + '52' + '  on  ' + str(now) + '\n'),
    aa2.close()
   bb52 = 1
#
 if (GPIO.input(25)) == 0:
   if bb53 == 1:
    aa2 = open(pwd2, 'a')
    aa2.write('<br />' + '53' + '  off  ' + str(now) + '\n'),
    aa2.close()
   bb53 = 0
 if (GPIO.input(25)) == 1:
   if bb53 == 0:
    aa2 = open(pwd2, 'a')
    aa2.write('<br />' + '53' + '  on  ' + str(now) + '\n'),
    aa2.close()
   bb53 = 1
#
 if (GPIO.input(24)) == 0:
   if bb54 == 1:
    aa2 = open(pwd2, 'a')
    aa2.write('<br />' + '54' + '  off  ' + str(now) + '\n'),
    aa2.close()
   bb54 = 0
 if (GPIO.input(24)) == 1:
   if bb54 == 0:
    aa2 = open(pwd2, 'a')
    aa2.write('<br />' + '54' + '  on  ' + str(now) + '\n'),
    aa2.close()
   bb54 = 1
#
 if (GPIO.input(23)) == 0:
   if bb55 == 1:
    aa2 = open(pwd2, 'a')
    aa2.write('<br />' + '55' + '  off  ' + str(now) + '\n'),
    aa2.close()
   bb55 = 0
 if (GPIO.input(23)) == 1:
   if bb55 == 0:
    aa2 = open(pwd2, 'a')
    aa2.write('<br />' + '55' + '  on  ' + str(now) + '\n'),
    aa2.close()
   bb55 = 1
#
 if (GPIO.input(22)) == 0:
   if bb56 == 1:
    aa2 = open(pwd2, 'a')
    aa2.write('<br />' + '56' + '  off  ' + str(now) + '\n'),
    aa2.close()
   bb56 = 0
 if (GPIO.input(22)) == 1:
   if bb56 == 0:
    aa2 = open(pwd2, 'a')
    aa2.write('<br />' + '56' + '  on  ' + str(now) + '\n'),
    aa2.close()
   bb56 = 1

 GPIO.output(3,False),
 GPIO.output(2,True),
 time.sleep(t)

 if (GPIO.input(27)) == 0:
   if bb61 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '61' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb61 = 0
 if (GPIO.input(27)) == 1:
   if bb61 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '61' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb61 = 1
#
 if (GPIO.input(26)) == 0:
   if bb62 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '62' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb62 = 0
 if (GPIO.input(26)) == 1:
   if bb62 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '62' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb62 = 1
#
 if (GPIO.input(25)) == 0:
   if bb63 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '63' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb63 = 0
 if (GPIO.input(25)) == 1:
   if bb63 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '63' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb63 = 1
#
 if (GPIO.input(24)) == 0:
   if bb64 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '64' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb64 = 0
 if (GPIO.input(24)) == 1:
   if bb64 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '64' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb64 = 1
#
 if (GPIO.input(23)) == 0:
   if bb65 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '65' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb65 = 0
 if (GPIO.input(23)) == 1:
   if bb65 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '65' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb65 = 1
#
 if (GPIO.input(22)) == 0:
   if bb66 == 1:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '66' + '  off  ' + str(now) + '\n'),
    a2.close()
   bb66 = 0
 if (GPIO.input(22)) == 1:
   if bb66 == 0:
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '66' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb66 = 1

 GPIO.output(2,False),

















