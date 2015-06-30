#!/usr/bin/env python2.7
import tweepy
import os
import pygame
import pygame.camera
import time
from pygame.locals import *
#from subprocess import call
from datetime import datetime

# Consumer keys and access tokens, used for OAuth
consumer_key = '63WqKRzO97p11lsLEGYAwo3Af'
consumer_secret = 'HyclLqDbmW4wfc9ymQFou8yTun9UgbvJOj8DeqFmDyK3ZxzV6e'
access_token = '2915347673-eMOG1zm4T0s5gt8IvwsLBIhQqiMRmBnJOpvWotx'
access_token_secret = 'rbiWHRDsl2y8wJSm6KqMambw5lPTYKPKcy3ls4oOZiCtl'

i = datetime.now()               #take time and date for filename
now = i.strftime('%Y%m%d-%H%M%S')
photo_name = now + '.jpg'
#cmd = 'raspistill -t 500 -w 1024 -h 768 -o /home/pi/' + photo_name 
#call ([cmd], shell=True)         #shoot the photo

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
#api.update_with_media(photo_path, status=status)
#api.update_status(status)

#get pic
photo_path = '/home/pi/tweetpi/' + photo_name
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(1024,768))
cam.start()
image = cam.get_image()
pygame.image.save(image, photo_path)
cam.stop()
from subprocess import call
photofile = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload " + photo_path + " " + photo_name
print photofile
#photofile = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/tweetpi/20141212-222857.jpg 20141212-222857.jpg"
call ([photofile], shell=True)

# Send the tweet with photo
#status = 'Photo auto-tweet from Pi: ' + i.strftime('%Y/%m/%d %H:%M:%S') + temp
#api.update_with_media(photo_path, status=status)
#api.update_status(status)





