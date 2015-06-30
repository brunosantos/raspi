import RPi.GPIO as GPIO
import os
import shlex, subprocess
from datetime import datetime
from remotealert import RemoteAlert


ra = RemoteAlert()
dev_id = '4d343079-7fd5-4a05-82f8-4179a48dc632'

def postAndroid(channel):
    #ra.send( dev_id, 'Message from pi' )    
    i = datetime.now()     
    message = 'Pi Alert: ' + i.strftime('%Y/%m/%d %H:%M:%S')
    ra.send( dev_id, message )

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "Waiting for falling edge on port 18"

try:
    GPIO.wait_for_edge(18, GPIO.FALLING)
    postAndroid('123');
    
    #GPIO.add_event_detect(18, GPIO.FALLING, callback=postAndroid, bouncetime=300)
    print "\nFalling edge detected. Now your program can continue with"
    print "whatever was waiting for a button press."
    
    while True:
        a= 123;
    
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit
GPIO.cleanup()           # clean up GPIO on normal exit
