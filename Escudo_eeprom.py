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


eeprom_I2C_ID=0x50              #eeprom I2C address
data= 10                        # data to be written
eeprom_reg_address=0
bus.write_byte_data(eeprom_I2C_ID,eeprom_reg_address,data)     # write data to eeprom

sleep(0.7)

while(1):

   read_data=bus.read_byte_data(eeprom_I2C_ID,eeprom_reg_address)   #read data from eeprom
   if(read_data==data):
       print "EEPROM WORKING"
