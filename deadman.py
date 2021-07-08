#!/usr/bin/python

# python2 not python3

# updated 2 Jan 2019 for second deadman signal
# second DM is a blinky attached to the UPS3 board
# updated 31 Dec 2018 for TCP socket watchdog

# 29 July 2018 - gswann
# deadman.py program to show
# cpu is running

# 2 June 2021 - gswann
# creating database lookup function to get port for hostname
# copied then merged with check_lightning

# rp5 is the new master since the exact same deadman.py is
# now run on multiple computers
# rp2 rp5 rp6 rp7 rp8

#global dmversion
#dmversion="1.1"

# 10 Jun 2021 - gswann
# adding broadcast function to search for watchdog server

# 18 Jun 2021 - gswann
# increased timeout to 10 seconds


#import pdb

from time import sleep
from datetime import datetime

import RPi.GPIO as GPIO
import socket

myHost=socket.gethostname()

debug = 1

mySleep = 5
myTimeout = 0

myPort=0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# real deadman for the UPS3
# GPIO13 - header pin33 - 4 up on left
pinDM = 13
GPIO.setup(pinDM,GPIO.OUT)

# blinky deadman for the green LED on UPS3
# GPIO6 - header pin31 - 5 up on left
pinDM2 = 6
GPIO.setup(pinDM2,GPIO.OUT)

import getport
import getwd


def checkin():
    global myTimeout
    global myPort
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    host = 'ha32163'
    host = serverHost

    port = myPort

    try:
       s.settimeout(10.0)
       s.connect((host, port))

       # Receive no more than 1024 bytes
       s.sendall(b'mysend')
       msg = s.recv(1024)
       s.close()
       print (serverHost + " " + msg.decode('ascii') + ' - ' + str(myTimeout) + ' errors')
    except:
          myTimeout += 1
          print('couldnt connect ' + str(myTimeout) + ' times' )


#pdb.set_trace()
serverHost=getwd.getserverhost()
myPort=getport.getport(serverHost,myHost)

checkin()

ctr = 0
while(1):

    ctr += 1
    if ctr == 3:
      ctr = 0
      checkin()

# real DM
    myState = GPIO.input(pinDM)
    GPIO.output(pinDM,  not myState)

# blinky DM
    for x in range(3):
      GPIO.output(pinDM2, 1)
      sleep(1)
      GPIO.output(pinDM2, 0)
      sleep(1)
    
    if (debug == 1):
        if (myState):
           print("tock.")
        else :
           print("tick.")
#    sleep(1)

