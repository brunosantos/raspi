#!/usr/bin/env python2.7
from twython import Twython
import os
import pygame
import pygame.camera
from pygame.locals import *
#from subprocess import call
from datetime import datetime

# Consumer keys and access tokens, used for OAuth
consumer_key = 'V3mUydORrcjV7zb8ZQko4Z7Ju'
consumer_secret = '1Mxwhe32gf5h5247ZepykkVn1bBce5YXgYJBIbHgJHpe4VIqnL'
access_token = '2915347673-eMOG1zm4T0s5gt8IvwsLBIhQqiMRmBnJOpvWotx'
access_token_secret = 'rbiWHRDsl2y8wJSm6KqMambw5lPTYKPKcy3ls4oOZiCtl'

i = datetime.now()               #take time and date for filename
now = i.strftime('%Y%m%d-%H%M%S')
photo_name = now + '.jpg'
#cmd = 'raspistill -t 500 -w 1024 -h 768 -o /home/pi/' + photo_name 
#call ([cmd], shell=True)         #shoot the photo

# OAuth process, using the keys and tokens
#api = Twython(consumer_key, consumer_secret,access_token,access_token_secret) 
api = Twython('V3mUydORrcjV7zb8ZQko4Z7Ju','1Mxwhe32gf5h5247ZepykkVn1bBce5YXgYJBIbHgJHpe4VIqnL','2915347673-eMOG1zm4T0s5gt8IvwsLBIhQqiMRmBnJOpvWotx','rbiWHRDsl2y8wJSm6KqMambw5lPTYKPKcy3ls4oOZiCtl') 

#Get Temperature
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]

# Send the tweet with photo
status = 'Photo auto-tweet from Pi: ' + i.strftime('%Y/%m/%d %H:%M:%S') + " " + temp

#get pic
photo_path = '/home/pi/tweetpi/' + photo_name
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(1024,768))
cam.start()
image = cam.get_image()
pygame.image.save(image, photo_path)

# Send the tweet with photo
photo = open(photo_path,'rb')
api.update_status_with_media(media=photo, status=status)

