try:
  import usocket as socket
except:
  import socket

from machine import Pin, Signal
import network
import time

import esp
esp.osdebug(None)

import gc
gc.collect()


ssid = 'your wifi gateway'
password = 'your password'
#due to a board using an active low signal we will invert from what normal examples show. Check out signal class in micropython
led_pin = Pin(2, Pin.OUT)
led = Signal(led_pin,invert=True)
led.off()
#create a station
station = network.WLAN(network.STA_IF)
#set the station as active
station.active(True)
#send connect to the wireless network
station.connect(ssid, password)
#this will run until the station is connected
while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

time.sleep(3)
print("Hello Sam!")
