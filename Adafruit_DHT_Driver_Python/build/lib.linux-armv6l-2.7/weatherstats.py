#!/usr/bin/env python

import os
import re
import xively
import subprocess
import time
import datetime
import sys
import dhtreader



FEED_ID=201742575
API_KEY="NyuTGZ6vSBsLvxXXOguBgpVHyAOGhx8CSmSOJm94jVDI22Z0"
DEBUG=True

# initialize api client
api = xively.XivelyAPIClient(API_KEY)

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
    print "Temperature: %.1f F" % temperature
    return {"temperature":temperature,"humidity":humidity}

    time.sleep(3)

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
    return {"tempds":temp_datastream, "humidityds":humidity_datastream}

def run():
    print "Starting environmental monitoring script"
    feed = api.feeds.get(FEED_ID)
    datastreams = get_datastream(feed)

    datastreams['tempds'].max_value = None
    datastreams['tempds'].min_value = None
    datastreams['humidityds'].min_value = None
    datastreams['humidityds'].min_value = None

    while True:
        try:
            dhtdata = read_dht()
                
        #if DEBUG:
            print "Updating Xively feed with temperature: %.2f F" % dhtdata['temperature']
            print "Updating Xively feed with humidity: %.2f percent" % dhtdata['humidity']
            datastreams['tempds'].current_value = dhtdata['temperature']
            datastreams['tempds'].at = datetime.datetime.utcnow()
            datastreams['tempds'].update()
            datastreams['humidityds'].current_value = dhtdata['humidity']
            datastreams['humidityds'].at = datetime.datetime.utcnow()
            datastreams['humidityds'].update()
            time.sleep(4)
        
        except:
            print "Error..."


run()