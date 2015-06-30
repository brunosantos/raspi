#!/usr/bin/env python

import time
import datetime
import xively
import RPi.GPIO as io
io.setmode(io.BOARD)
 
pir_pin = 16
 
io.setup(pir_pin, io.IN)         # activate input

FEED_ID=201742575
API_KEY="NyuTGZ6vSBsLvxXXOguBgpVHyAOGhx8CSmSOJm94jVDI22Z0"
DEBUG=True

# initialize api client
#api = xively.XivelyAPIClient(API_KEY)
#feed = api.feeds.get(FEED_ID)

try:
#    pir_datastream = feed.datastreams.get("rxs")
    if DEBUG:
        print "Found existing pir datastream"
except:
    if DEBUG:
        print "Creating new pir datastream"
#        pir_datastream = feed.datastreams.create("rxs", tags="rxs")
        
print "Starting environmental monitoring script"

#datastreams =  {"rxs":pir_datastream}

#datastreams['rxs'].max_value = 1
#datastreams['rxs'].min_value = 0
 
while True:
    if io.input(pir_pin):
        #print("PIR ALARM!")
        pir_data=1
    else:
        pir_data=0
        
    #print "Updating Xively feed with pir: %d " % pir_data
#    datastreams['rxs'].current_value = pir_data
#    datastreams['rxs'].at = datetime.datetime.utcnow()
#    datastreams['rxs'].update()    
    print(pir_data),
    time.sleep(0.000222)#222000ns - 
    