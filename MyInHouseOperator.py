#!/usr/bin/python
# -*- coding: utf-8 -*-

#ttyname = "tty0"
ttyname = "ttyACM0"

def main():
    syslogTempture()

import syslog
def syslogTempture():
    tempture = getTempture()
    #syslog.openlog(logopt=syslog.LOG_PID|syslog.LOG_PERROR)
    syslog.openlog()
    syslog.syslog('Current tempture :\t' + tempture)
    syslog.closelog()

import serial
def getTempture():
    ser=serial.Serial(port = '/dev/' + ttyname,\
                          baudrate = 9600,\
                          parity = serial.PARITY_NONE,\
                          bytesize = serial.EIGHTBITS,\
                          stopbits = serial.STOPBITS_ONE,\
                          timeout = None,\
                          xonxoff = 0,\
                          rtscts = 0,\
                          #    interCharTimeout = None
                      )
    ser.open()
    ser.write("temp")
    msg = ser.readline()
    msg.replace("\t" , "")
    while not msg.endswith("Cel"):
        msg = ser.readline()
    ser.close()
    return msg

main()
