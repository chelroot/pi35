#! /usr/bin/env python
# coding: utf-8


import sys
 
fname = '/var/www/html/a2.html'
lines = 0
words = 0
letters = 0
 
for line in open(fname):
    lines += 1
 
print("Lines:", lines)
