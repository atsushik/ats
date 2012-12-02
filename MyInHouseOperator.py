#!/usr/bin/python
# -*- coding: utf-8 -*-

#ttyname = "tty0"
ttyname = "ttyACM0"

def main():
    syslogTempture()
    syslogBrightness()

import syslog
def syslogTempture():
    temperature = getSensorData("temperature")
    #syslog.openlog(logopt=syslog.LOG_PID|syslog.LOG_PERROR)
    syslog.openlog()
    syslog.syslog('Current temperature : ' + temperature + " Celcius")
    syslog.closelog()

def syslogBrightness():
    brightness = getSensorData("brightness")
    #syslog.openlog(logopt=syslog.LOG_PID|syslog.LOG_PERROR)
    syslog.openlog()
    syslog.syslog('Current brightness : ' + brightness + " lx")
    syslog.closelog()

import serial
def getSensorData(sensorType):
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
    ser.write(sensorType)
    msg = ser.readline()
    while not msg.startswith(sensorType):
        msg = ser.readline()
    ser.close()
    msg = msg.strip()
    #print msg.split(" ")
    return msg.split(" ")[1]

main()
