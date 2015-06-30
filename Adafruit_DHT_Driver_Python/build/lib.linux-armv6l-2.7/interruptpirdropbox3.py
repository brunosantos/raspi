#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv/
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
import RPi.GPIO as GPIO
import os
import io
import shlex, subprocess
import tweepy
import pygame
import pygame.camera
from pygame.locals import *
from datetime import datetime

def go():
    # Consumer keys and access tokens, used for OAuth
    consumer_key = 'V3mUydORrcjV7zb8ZQko4Z7Ju'
    consumer_secret = '1Mxwhe32gf5h5247ZepykkVn1bBce5YXgYJBIbHgJHpe4VIqnL'
    access_token = '2915347673-eMOG1zm4T0s5gt8IvwsLBIhQqiMRmBnJOpvWotx'
    access_token_secret = 'rbiWHRDsl2y8wJSm6KqMambw5lPTYKPKcy3ls4oOZiCtl'
    
    i = datetime.now()               #take time and date for filename
    now = i.strftime('%Y%m%d-%H%M%S')
    photo_name = now + '.jpg'
    
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)
    
    #Get Temperature
    cmd = '/opt/vc/bin/vcgencmd measure_temp'
    line = os.popen(cmd).readline().strip()
    temp = line.split('=')[1].split("'")[0]
    
    # Send the tweet with photo
    status = 'Photo auto-tweet from Pi: ' + i.strftime('%Y/%m/%d %H:%M:%S') + temp    
    api.update_status(status=status)

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN)

print "During this waiting time, your computer is not" 
print "wasting resources by polling for a button press.\n"

try:
    while True:
        go()    
        
        
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit

finally:
    GPIO.cleanup() # ensures a clean exit    
