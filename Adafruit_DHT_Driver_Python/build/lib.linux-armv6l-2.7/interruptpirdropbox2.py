#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv/
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
import RPi.GPIO as GPIO
import os
import io
import shlex, subprocess
import tweet

GPIO.setmode(GPIO.BCM)


GPIO.setup(18, GPIO.IN)

print "During this waiting time, your computer is not" 
print "wasting resources by polling for a button press.\n"

try:
    while True:
        #GPIO.wait_for_edge(18, GPIO.RISING)
        print "\nFalling edge detected. Now your program can continue with"
        print "whatever was waiting for a button press."
        if GPIO.input(18):
            print("PIR ALARM!")
            #tweetPic4.go()  
            #return 1
        #return 0    
	tweet.go()        
        
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit

finally:
    GPIO.cleanup() # ensures a clean exit    
