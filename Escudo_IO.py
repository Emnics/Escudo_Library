"""***********************************************************************
Author      : 
Organization:  Emnics Technologies Pvt Ltd
Description :  Sample code for all the available GPIOs in ESCUDO
***********************************************************************"""

import RPi.GPIO as GPIO
from time import sleep
import os
import smbus
import thread
bus=smbus.SMBus(1)                     #I2C Library 
GPIO.setmode(GPIO.BOARD)               #Pin No Selection based on Board

GPIO.setwarnings(False)

"""****************Pin Assignment************************************"""
RELAY = [7,11,12,13,15,16,18,24]       #Relay Pin Nos
INPUT =[40,37,38,35,36,33,31,32]       #Input Pin Nos
LED = [29]                             #LED Pin No
BUZZER = [22]                          #Buzzer Pin No
"""******************************************************************"""


"""*****************Pin Direction (Output/Input)**********************"""
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
GPIO.setup(18,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

GPIO.setup(40,GPIO.IN)
GPIO.setup(37,GPIO.IN)
GPIO.setup(38,GPIO.IN)
GPIO.setup(35,GPIO.IN)
GPIO.setup(36,GPIO.IN)
GPIO.setup(33,GPIO.IN)
GPIO.setup(31,GPIO.IN)
GPIO.setup(32,GPIO.IN)
"""*********************************************************************"""

"""************************SPI Pin Assignment**************************"""
SPICLK=23
SPIMOSI=19
SPIMISO=21
SPICS=26

GPIO.setup(SPIMOSI,GPIO.OUT)
GPIO.setup(SPIMISO,GPIO.IN)
GPIO.setup(SPICLK,GPIO.OUT)
GPIO.setup(SPICS,GPIO.OUT)
"""*********************************************************************"""

GPIO.output(BUZZER[0],False )            # Buzzer Turned OFF by default
address=0x68                             # RTC Register Address                  
address1=0x50                            # EEPROM Register Address



#""*********************************************************************"""
#Function Name   :Turn_ON_Buzzer
#Descriptions    :Turns ON Buzzer, Buzzer PIN becomes high
#Argument        :NA
#Return          :NA
"**************************************************************************"
def Turn_ON_Buzzer():
    GPIO.output(BUZZER[0],True)

#"""********************************************************************""""



#""*********************************************************************"""
#Function Name   :Turn_OFF_Buzzer
#Descriptions    :Turns OFF Buzzer, Buzzer PIN becomes LOW
#Argument        :NA
#Return          :NA
"*********************************************************************"""

def Turn_OFF_Buzzer():
    GPIO.output(BUZZER[0],False)

#""********************************************************************""""

#"""""*********************************************************************"""
#Function Name   :Turn_ON_Relay(relay_no)
#Descriptions    :Turns ON corresponding Relays. Relay Pin goes high
#Argument        :relay_no (Relay Number between 1 to 8)
#Return          :NA
"***********************************************************************"""

def Turn_ON_Relay(relay_no):
    relay_no=relay_no-1
    if((relay_no>7)or (relay_no<0)):
        print("please rnter correct relay noumber between 1 to 8")
    else:
       GPIO.output(RELAY[relay_no],True)

#"""********************************************************************""""


#"""*********************************************************************"""
#Function Name   :Turn_ON_Relay(relay_no)
#Descriptions    :Turns ON corresponding Relays. Relay Pin goes high
#Argument        :relay_no (Relay Number between 1 to 8)
#Return          :NA
"***********************************************************************"""

def Turn_OFF_Relay(relay_no):
    relay_no=relay_no-1
    if((relay_no>7) or (relay_no<0)):
        print("please rnter correct relay noumber between 1 to 8")
    else:
       GPIO.output(RELAY[relay_no],False)
       
#"""********************************************************************""""


#"""*********************************************************************"""
#Function Name   :LED_ON
#Descriptions    :LED Turns ON, Led pin goes high
#Argument        :none
#Return          :none
"***********************************************************************"""
def LED_ON():
    GPIO.output(LED[0],True)

#"""********************************************************************""""

#"""*********************************************************************"""
#Function Name   :LED_OFF
#Descriptions    :LED Turns OFF, Led pin goes Low
#Argument        :none
#Return          :none
"***********************************************************************"""

def LED_OFF():
    GPIO.output(LED[0],False)
    
#"""********************************************************************""""

#"""*********************************************************************"""
#Function Name   :Read_Input(input_no)
#Descriptions    :Reads corresponding input ie high or low
#Argument        :input_no (Input Number to be read between 1 to 8)
#Return          :none
"***********************************************************************"""

def Read_Input(input_no):
    input_no=input_no-1
    if((input_no>7) or (input_no<0)):
        print("please rnter correct input noumber between 1 to 8")
        return 
    if(GPIO.input(INPUT[input_no])==0):
       input_data=0
    else:
       input_data=1
    return input_data
#"""********************************************************************""""

while(1):
    LED_ON()
    Turn_ON_Buzzer()
    sleep(0.5)
    Turn_OFF_Buzzer()
    LED_OFF()
    if(0==Read_Input(3)):
            print "sw ON"
            Turn_ON_Relay(3)
     else:
            print  "sw off"
            Turn_OFF_Relay(3)
    

