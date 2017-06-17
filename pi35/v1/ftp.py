#! /usr/bin/env python
# coding: utf-8



import os, sys, os.path


#from ftplib import FTP
import ftplib

os.chdir('/var/www/html/')
file2a = "a2.html"
file11 = "d11.html"
file12 = "d12.html"
file21 = "d21.html"
file22 = "d22.html"
file23 = "d23.html"
file31 = "d31.html"
file32 = "d32.html"
file33 = "d33.html"
 
host = "10.10.0.34"
ftp_user = "vova"
ftp_password = "333"

con = ftplib.FTP(host, ftp_user, ftp_password)

# Открываем файл для передачи в бинарном режиме
f = open(file2a, "rb")
# Передаем файл на сервер
send = con.storbinary("STOR "+ file2a, f)

f = open(file11, "rb")
send = con.storbinary("STOR "+ file11, f)

f = open(file12, "rb")
send = con.storbinary("STOR "+ file12, f)

f = open(file21, "rb")
send = con.storbinary("STOR "+ file21, f)

f = open(file22, "rb")
send = con.storbinary("STOR "+ file22, f)

f = open(file23, "rb")
send = con.storbinary("STOR "+ file23, f)

f = open(file31, "rb")
send = con.storbinary("STOR "+ file31, f)

f = open(file32, "rb")
send = con.storbinary("STOR "+ file32, f)

f = open(file33, "rb")
send = con.storbinary("STOR "+ file33, f)


# Закрываем FTP соединение
con.close


