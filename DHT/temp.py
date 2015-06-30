#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import dhtreader

DHT11 = 11
DHT22 = 22
AM2302 = 22


dhtreader.init()

t, h = dhtreader.read(22, 4)
if t and h:
    print("Temp = {0} *C, Hum = {1} %".format(t, h))
else:
    print("Failed to read from sensor, maybe try again?")
