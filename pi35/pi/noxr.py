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
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)     # подтяжка к питанию
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

pwd1 = "/var/www/html/n2.html"

a2 = open(pwd1, 'a')

GPIO.output(8,False)
time.sleep(1)
GPIO.output(9,False)
time.sleep(1)
GPIO.output(8,False)
time.sleep(1)
GPIO.output(9,False)

def mfof(n):
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '%s' % n + '  off ' + str(now) + '\n'),
    a2.close()

def mfon(n):
    GPIO.output(9,True)
    GPIO.output(8,True)
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '%s' % n + '  on  ' + str(now) + '\n'),
    a2.close()

def dof(n):
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '%s' % n + '  off ' + str(now) + '\n'),
    a2.close()
    GPIO.output(8,False)
    
def don(n):
    GPIO.output(9,True)
    GPIO.output(8,True)
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '%s' % n + '  on  ' + str(now) + '\n'),
    a2.close()





while True :
 now = datetime.now()
 GPIO.output(7,True),
 time.sleep(t)

 if (GPIO.input(27)) == 0:
   if bb11 == 1:
    mfof(11)
   bb11 = 0
 if (GPIO.input(27)) == 1:
   if bb11 == 0:
    mfon(11)
   bb11 = 1
 if (GPIO.input(26)) == 0:
   if bb12 == 1:
    mfof(12)
   bb12 = 0
 if (GPIO.input(26)) == 1:
   if bb12 == 0:
    mfon(12)
   bb12 = 1
 if (GPIO.input(25)) == 0:
   if bb13 == 1:
    mfof(13)
   bb13 = 0
 if (GPIO.input(25)) == 1:
   if bb13 == 0:
    mfon(13)
   bb13 = 1
 if (GPIO.input(24)) == 0:
   if bb14 == 1:
    mfof(14)
   bb14 = 0
 if (GPIO.input(24)) == 1:
   if bb14 == 0:
    mfon(14)
   bb14 = 1
 if (GPIO.input(23)) == 0:
   if bb15 == 1:
    mfof(15)
   bb15 = 0
 if (GPIO.input(23)) == 1:
   if bb15 == 0:
    mfon(15)
   bb15 = 1
 if (GPIO.input(22)) == 0:
   if bb16 == 1:
    mfof(16)
   bb16 = 0
 if (GPIO.input(22)) == 1:
   if bb16 == 0:
    mfon(16)
   bb16 = 1

 GPIO.output(7,False),
 GPIO.output(6,True),
 time.sleep(t)
 if (GPIO.input(27)) == 0:
   if bb21 == 1:
    mfof(21)
   bb21 = 0
 if (GPIO.input(27)) == 1:
   if bb21 == 0:
    mfon(21)
   bb21 = 1
 if (GPIO.input(26)) == 0:
   if bb22 == 1:
    mfof(22)
   bb22 = 0
 if (GPIO.input(26)) == 1:
   if bb22 == 0:
    mfon(22)
   bb22 = 1
 if (GPIO.input(25)) == 0:
   if bb23 == 1:
    mfof(23)
   bb23 = 0
 if (GPIO.input(25)) == 1:
   if bb23 == 0:
    mfon(23)
   bb23 = 1
 if (GPIO.input(24)) == 0:
   if bb24 == 1:
    dof(24)
   bb24 = 0
 if (GPIO.input(24)) == 1:
   if bb24 == 0:
    don(24) 
   bb24 = 1
 if (GPIO.input(23)) == 0:
   if bb25 == 1:
    dof(25)
   bb25 = 0
 if (GPIO.input(23)) == 1:
   if bb25 == 0:
    don(25)
   bb25 = 1
 if (GPIO.input(22)) == 0:
   if bb26 == 1:
    mfof(26)
   bb26 = 0
 if (GPIO.input(22)) == 1:
   if bb26 == 0:
    mfon(26)
   bb26 = 1

 GPIO.output(6,False),
 GPIO.output(5,True),
 time.sleep(t)
 if (GPIO.input(27)) == 0:
   if bb31 == 1:
    mfof(31)
   bb31 = 0
 if (GPIO.input(27)) == 1:
   if bb31 == 0:
    mfon(31)
   bb31 = 1
 if (GPIO.input(26)) == 0:
   if bb32 == 1:
    mfof(32)
   bb32 = 0
 if (GPIO.input(26)) == 1:
   if bb32 == 0:
    GPIO.output(9,True)
    mfon(32)
   bb32 = 1
 if (GPIO.input(25)) == 0:
   if bb33 == 1:
    mfof(33)
   bb33 = 0
 if (GPIO.input(25)) == 1:
   if bb33 == 0:
    GPIO.output(9,True)
    mfon(33) 
   bb33 = 1
 if (GPIO.input(24)) == 0:
   if bb34 == 1:
    mfof(34)
   bb34 = 0
 if (GPIO.input(24)) == 1:
   if bb34 == 0:
#    mfon(34)
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '34' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb34 = 1
 if (GPIO.input(23)) == 0:
   if bb35 == 1:
    mfof(35)
   bb35 = 0
 if (GPIO.input(23)) == 1:
   if bb35 == 0:
    mfon(35);
   bb35 = 1
 if (GPIO.input(22)) == 0:
   if bb36 == 1:
    mfof(36)
   bb36 = 0
 if (GPIO.input(22)) == 1:
   if bb36 == 0:
    mfon(36); 
   bb36 = 1

 GPIO.output(5,False),
 GPIO.output(4,True),
 time.sleep(t)
 if (GPIO.input(27)) == 0:
   if bb41 == 1:
    mfof(41)
   bb41 = 0
 if (GPIO.input(27)) == 1:
   if bb41 == 0:
    mfon(41)
   bb41 = 1
 if (GPIO.input(26)) == 0:
   if bb42 == 1:
    mfof(42)
   bb42 = 0
 if (GPIO.input(26)) == 1:
   if bb42 == 0:
    mfon(42)
   bb42 = 1
 if (GPIO.input(25)) == 0:
   if bb43 == 1:
    mfof(43)
   bb43 = 0
 if (GPIO.input(25)) == 1:
   if bb43 == 0:
    mfon(43)
   bb43 = 1
 if (GPIO.input(24)) == 0:
   if bb44 == 1:
    dof(44)
   bb44 = 0
 if (GPIO.input(24)) == 1:
   if bb44 == 0:
    don(44)
   bb44 = 1
 if (GPIO.input(23)) == 0:
   if bb45 == 1:
    dof(45)
   bb45 = 0
 if (GPIO.input(23)) == 1:
   if bb45 == 0:
#    don(45)
    a2 = open(pwd1, 'a')
    a2.write('<br />' + '45' + '  on  ' + str(now) + '\n'),
    a2.close()
   bb45 = 1
 if (GPIO.input(22)) == 0:
   if bb46 == 1:
    dof(46)
   bb46 = 0
 if (GPIO.input(22)) == 1:
   if bb46 == 0:
    don(46)
   bb46 = 1

 GPIO.output(4,False),
 GPIO.output(3,True),
 time.sleep(t)

 if (GPIO.input(27)) == 0:
   if bb51 == 1:
    mfof(51)
   bb51 = 0
 if (GPIO.input(27)) == 1:
   if bb51 == 0:
    mfon(51)
   bb51 = 1
 if (GPIO.input(26)) == 0:
   if bb52 == 1:
    mfof(52)
   bb52 = 0
 if (GPIO.input(26)) == 1:
   if bb52 == 0:
    mfon(52) 
   bb52 = 1
 if (GPIO.input(25)) == 0:
   if bb53 == 1:
    mfof(53)
   bb53 = 0
 if (GPIO.input(25)) == 1:
   if bb53 == 0:
    mfon(53)
   bb53 = 1
 if (GPIO.input(24)) == 0:
   if bb54 == 1:
    mfof(54)   
   bb54 = 0
 if (GPIO.input(24)) == 1:
   if bb54 == 0:
    mfon(54)
   bb54 = 1
   GPIO.output(8,True),
 if (GPIO.input(23)) == 0:
   if bb55 == 1:
    mfof(55)
   bb55 = 0
 if (GPIO.input(23)) == 1:
   if bb55 == 0:
    mfon(55)
   bb55 = 1
 if (GPIO.input(22)) == 0:
   if bb56 == 1:
    mfof(56) 
   bb56 = 0
 if (GPIO.input(22)) == 1:
   if bb56 == 0:
    mfon(56)
   bb56 = 1


 GPIO.output(3,False),
 GPIO.output(2,True),
 time.sleep(t)

 if (GPIO.input(27)) == 0:
   if bb61 == 1:
    a2.write('<br />' + '61' + '  off ' + str(now) + '\n'),
   bb61 = 0
 if (GPIO.input(27)) == 1:
   if bb61 == 0:
    a2.write('<br />' + '61' + '  on  ' + str(now) + '\n'),
    bb61 = 1
 if (GPIO.input(26)) == 0:
   if bb62 == 1:
    a2.write('<br />' + '62' + '  off ' + str(now) + '\n'),
   bb62 = 0
 if (GPIO.input(26)) == 1:
   if bb62 == 0:
    a2.write('<br />' + '62' + '  on  ' + str(now) + '\n'),
   bb62 = 1
 if (GPIO.input(25)) == 0:
   if bb63 == 1:
    a2.write('<br />' + '63' + '  off ' + str(now) + '\n'),
   bb63 = 0
 if (GPIO.input(25)) == 1:
   if bb63 == 0:
    a2.write('<br />' + '63' + '  on  ' + str(now) + '\n'),
   bb63 = 1
 if (GPIO.input(24)) == 0:
   if bb64 == 1:
    mfof(64)
   bb64 = 0
 if (GPIO.input(24)) == 1:
   if bb64 == 0:
    mfon(64)
   bb64 = 1
 if (GPIO.input(23)) == 0:
   if bb65 == 1:
    mfof(65)
   bb65 = 0
 if (GPIO.input(23)) == 1:
   if bb65 == 0:
    mfon(65)
   bb65 = 1
 if (GPIO.input(22)) == 0:
   if bb66 == 1:
    mfof(66)
   bb66 = 0
 if (GPIO.input(22)) == 1:
   if bb66 == 0:
    mfon(66)
   bb66 = 1

 GPIO.output(2,False),
 
