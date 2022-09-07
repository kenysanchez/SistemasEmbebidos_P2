#!/usr/bin/env python
from grovepi import *
import grovepi
from grove_rgb_lcd import *
import time

button = 4      #Port for Button
sensor = 0      # Analog A0

pinMode(button,"INPUT")     # Assign mode for Button as input

while True:
    button_status= digitalRead(button)  #Read the Button status
    if button_status:   #If the Button is in HIGH position, run the program
    #Boton presionado
        temp = grovepi.temp(sensor,'1')
        setText("Temp = " + str(temp))
        setRGB(0,255,0)
        time.sleep(.5)
        
    else:
    #If Button is in Off position, print "Off" on the screen
        setText("Presiona el/n boton")
        setRGB(255,0,0)