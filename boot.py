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
import ntptime

import esp
esp.osdebug(None)

import gc
gc.collect()

with open('settings.json', 'r') as f:
  settings_dict = json.load(f)

print(settings_dict)

#TODO: need to add a read from a json config file that will live on the board
ssid = settings_dict['SSID']
password = settings_dict['Key']
#create a station
station = network.WLAN(network.STA_IF)
#set the station as active
station.active(True)

def wifiConnect():
  print(ssid)
  print(password)
  #send connect to the wireless network
  station.connect(ssid, password)
  #this will run until the station is connected
  while station.isconnected() == False:
    pass
  
#due to a board using an active low signal we will invert from what normal examples show. Check out signal class in micropython
led_pin = Pin(2, Pin.OUT)
led = Signal(led_pin,invert=False)
led.off()

MOTOR_PIN1 = machine.Pin(4, machine.Pin.OUT)
MOTOR_PIN2 = machine.Pin(5, machine.Pin.OUT)
MOTOR_FREQUENCY = 15000
MOTOR_PWM = machine.PWM(machine.Pin(13), MOTOR_FREQUENCY)
dc_motor = DCMotor(MOTOR_PIN1, MOTOR_PIN2, MOTOR_PWM)
led_state = settings_dict['LEDState']
door_state = settings_dict['DoorState']
color = "000000"
print(led_state)
print(door_state)

print('Connecting to Wifi')
wifiConnect()

print('Connection successful')
print(station.ifconfig())

time.sleep(3)
print("Hello Sam!")