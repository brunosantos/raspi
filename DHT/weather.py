#!/usr/bin/env python
import os
import re
import xively
import subprocess
import time
import datetime
import sys
import dhtreader
import RPi.GPIO as io

FEED_ID=201742575
API_KEY="NyuTGZ6vSBsLvxXXOguBgpVHyAOGhx8CSmSOJm94jVDI22Z0"
DEBUG=True

# initialize api client
api = xively.XivelyAPIClient(API_KEY)
    
#io.setmode(io.BOARD)
#io.cleanup()

pir_pin = 12

def read_dht():
    if DEBUG:
        print "reading dht temperature and humidity"

    dhtreader.init()

    t, h = dhtreader.read(22, 4)
    if t and h:
        print("Temp = {0} *C, Hum = {1} %".format(t, h))
    else:
        print("Failed to read from sensor, maybe try again?")


# search for humidity 
    humidity = round(float(h),2)
    #if DEBUG:
    print "Humidity: %.1f %%" % humidity

# search for temperature 
    temperature =  round(float(t),2)#float(h)*(9.0/5.0) + 32
   # if DEBUG:
    print "Temperature: %.1f C" % temperature
    return {"temperature":temperature,"humidity":humidity}

    time.sleep(4)
    
def get_pir(): 
    io.setmode(io.BOARD)
    io.setup(pir_pin, io.IN)         # activate input
 
    if io.input(pir_pin):
        print("PIR ALARM!")
        return 1
    return 0
    #time.sleep(0.5)

def get_datastream(feed):
    try:
        temp_datastream = feed.datastreams.get("temperature")
        if DEBUG:
            print "Found existing temperature datastream"
    except:
        if DEBUG:
            print "Creating new temperature datastream"
            temp_datastream = feed.datastreams.create("temperature", tags="temperature")

    try:
        humidity_datastream = feed.datastreams.get("humidity")
        if DEBUG:
            print "Found existing humidity datastream"
    except:
        if DEBUG:
            print "Creating new humidity datastream"
            humidity_datastream = feed.datastreams.create("humidity", tags="humidity")
            
    try:
        pir_datastream = feed.datastreams.get("pir")
        if DEBUG:
            print "Found existing pir datastream"
    except:
        if DEBUG:
            print "Creating new pir datastream"
            pir_datastream = feed.datastreams.create("pir", tags="pir")
            
    return {"tempds":temp_datastream, "humidityds":humidity_datastream, "pirds":pir_datastream}

def run():
    if DEBUG:
         print "debug mode on"
    print "Starting environmental monitoring script"
    feed = api.feeds.get(FEED_ID)
    datastreams = get_datastream(feed)

    datastreams['tempds'].max_value = 50
    datastreams['tempds'].min_value = -10
    datastreams['tempds'].unit = "% [+-5]"
    
    datastreams['humidityds'].min_value = 100
    datastreams['humidityds'].min_value = 0
    datastreams['humidityds'].unit = "% [2-5]"
    
    datastreams['pirds'].max_value = 1
    datastreams['pirds'].min_value = 0

    while True:
        try:
            dhtdata = read_dht()
            time.sleep(0.5)
            pir_data = get_pir()
            
            if DEBUG:
                print "Updating Xively feed with temperature: %.2f C" % dhtdata['temperature']
                print "Updating Xively feed with humidity: %.2f percent" % dhtdata['humidity']
            
            datastreams['tempds'].current_value = dhtdata['temperature']
            datastreams['tempds'].at = datetime.datetime.utcnow()
            datastreams['tempds'].update()
            
            datastreams['humidityds'].current_value = dhtdata['humidity']
            datastreams['humidityds'].at = datetime.datetime.utcnow()
            datastreams['humidityds'].update()
            
            if DEBUG:
                print "Updating Xively feed with pir: %d " % pir_data
            datastreams['pirds'].current_value = pir_data
            datastreams['pirds'].at = datetime.datetime.utcnow()
            datastreams['pirds'].update()
            
            time.sleep(5)
        
        except:
            print "Error..."
            #io.cleanup()


run()
io.cleanup()
