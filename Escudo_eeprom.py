"""***********************************************************************
Author      : 
Organization:  Emnics Technologies Pvt Ltd
Description :  Sample code for ESCUDO EEPROM 
***********************************************************************"""
import RPi.GPIO as GPIO
from time import sleep
import os
import smbus
import thread
bus=smbus.SMBus(1)
GPIO.setmode(GPIO.BOARD)

address1=0x50                            # EEPROM Register Address

#"""*********************************************************************"""
#Function Name   :Save_To_Memory(addr,data)
#Descriptions    :Saves Data to memory
#Argument        :Address,Data
#Return          :None
"***********************************************************************"""

def Save_To_Memory(addr,data):
    bus.write_byte_data(address1,0,0xA0)
    sleep(0.7)
    bus.write_byte_data(address1,addr,data)
    sleep(0.7)
#"""********************************************************************""""
   
#"""*********************************************************************"""
#Function Name   :Read_From_Memory(addr)
#Descriptions    :Reads Data from memory
#Argument        :Address
#Return          :Data
"***********************************************************************"""

def Read_From_Memory(addr):
     data=bus.read_byte_data(address1,addr)
     sleep(0.7)
     return data

#"""********************************************************************""""

Save_To_Memory(2,10)
while(1):
     x=Read_From_Memory(2)
     print x
   
