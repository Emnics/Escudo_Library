
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

address=0x68                 # RTCC Reg address

#"""*********************************************************************"""
#Function Name   :Set_Time
#Descriptions    :Resets RTC default Timings
#Argument        :hour,minute,second
#Return          :None
"***********************************************************************"""

def Set_Time(hour,minute,second):
    SEC_ONTIME=second
    MIN_ONTIME=minute
    HR_ONTIME=hour
    bus.write_byte_data(address,0,0xD0)
    sleep(0.7)
    SEC_ONTIME=(((SEC_ONTIME/10)<<4)+(SEC_ONTIME%10))
    bus.write_byte_data(address,0,SEC_ONTIME)
    sleep(0.7)
    MIN_ONTIME=(((MIN_ONTIME/10)<<4)+(MIN_ONTIME%10))
    bus.write_byte_data(address,1,MIN_ONTIME)
    sleep(0.7)
    HR_ONTIME=(((HR_ONTIME/10)<<4)+(HR_ONTIME%10))
    bus.write_byte_data(address,2,HR_ONTIME)
    sleep(0.7)
#"""********************************************************************""""


#"""*********************************************************************"""
#Function Name   :Read_Time
#Descriptions    :Reads current RTCC Time
#Argument        :None
#Return          :Time (hr:min:sec formar) 
"***********************************************************************"""

def Read_Time():
    col=bus.read_byte_data(address,0)
    col=(((col>>4)*10)+(col&0x0f))
    mint=bus.read_byte_data(address,1)
    mint=(((mint>>4)*10)+(mint&0x0f))
    hr=bus.read_byte_data(address,2)
    hr=(((hr>>4)*10)+(hr&0x0f))
    return str(hr)+":"+str(mint)+":"+str(col)
#"""********************************************************************""""

Set_Time(14,30,0)
while(1):
     time=Read_From_Memory(2)
     print time

