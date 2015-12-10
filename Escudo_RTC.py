
"""***********************************************************************
Author      : 
Organization:  Emnics Technologies Pvt Ltd
Description :  Sample code for ESCUDO RTCC
***********************************************************************"""

#---------Import all required libraries--------------------#
import RPi.GPIO as GPIO
from time import sleep
import os
import smbus                  #library for I2C Operation
import thread
bus=smbus.SMBus(1)
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

address=0x68                 # RTCC I2C slave ID

#-----------Function to read time from RTCC--------------------#
def Read_Time():
    col=bus.read_byte_data(address,0)
    col=(((col>>4)*10)+(col&0x0f))
    mint=bus.read_byte_data(address,1)
    mint=(((mint>>4)*10)+(mint&0x0f))
    hr=bus.read_byte_data(address,2)
    hr=(((hr>>4)*10)+(hr&0x0f))
    return str(hr)+":"+str(mint)+":"+str(col)
    
#---------------------------------------------------------------#

#---------------Function to set RTCC Time-----------------------#

def Set_Time(hour,minute,second):  
    bus.write_byte_data(address,0,0xD0)
    sleep(0.7)
    second=(((second/10)<<4)+(second%10))
    bus.write_byte_data(address,0,second)
    sleep(0.7)
    minute=(((minute/10)<<4)+(minute%10))
    bus.write_byte_data(address,1,minute)
    sleep(0.7)
    hour=(((hour/10)<<4)+(hour%10))
    bus.write_byte_data(address,2,hour)
    sleep(0.7)
#-----------------------------------------------------------------#    

Set_Time(12,0,0)                     #set time initially

while(1):
   RTCTime = Read_Time()            #Read Time
   print RTCTime                    #print time
   sleep(1)
   
#---------------------------EOF-------------------------------------#
