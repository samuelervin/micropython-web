try:
  import usocket as socket
except:
  import socket
import os
import json
import machine
import network
import time
from dcmotor import DCMotor    
from machine import Pin, Signal,PWM
import asyncio
import ntptime

import esp
esp.osdebug(None)

import gc
gc.collect()

#TODO: need to add a read from a json config file that will live on the board
ssid = 'yourssid'
password = 'yourpassword'

with open('settings.json', 'r') as f:
  settings_dict = json.load(f)
print(settings_dict)

#due to a board using an active low signal we will invert from what normal examples show. Check out signal class in micropython
led_pin = Pin(2, Pin.OUT)
led = Signal(led_pin,invert=True)
led.off()
#create a station
station = network.WLAN(network.STA_IF)
#set the station as active
station.active(True)

def wifiConnect():
  #send connect to the wireless network
  station.connect(ssid, password)
  #this will run until the station is connected
  while station.isconnected() == False:
    pass


wifiConnect()

print('Connection successful')
print(station.ifconfig())

time.sleep(3)
print("Hello Sam!")