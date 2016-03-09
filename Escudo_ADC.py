
import RPi.GPIO as GPIO
from time import sleep
import os
import smbus
import thread
bus=smbus.SMBus(1)                     #I2C Library 
GPIO.setmode(GPIO.BOARD)               #Pin No Selection based on Board

GPIO.setwarnings(False)


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


#---------------ADC read Function definition--------------------#
#function Name        : readadc
#arguments            : ADC number(between 1-8)
#return                : adc value
#---------------------------------------------------------------#

def readadc(adcnum):
     adcnum=adcnum-1
    clockpin=SPICLK
    mosipin=SPIMOSI
    misopin=SPIMISO
    cspin= SPICS
    
    if((adcnum>7) or (adcnum<0)):
        return -1
    GPIO.output(cspin,True)
    GPIO.output(clockpin,False)
    GPIO.output(cspin,False)
    commandout=adcnum
    commandout|=0x18
    commandout<<=3

    for i in range(5):
        if(commandout & 0x80):
            GPIO.output(mosipin,True)
        else:
            GPIO.output(mosipin,False)
        commandout<<=1
        GPIO.output(clockpin,True)
        GPIO.output(clockpin,False)

    adcout=0

    for i in range(12):
        GPIO.output(clockpin,True)
        GPIO.output(clockpin,False)
        adcout<<=1
        if(GPIO.input(misopin)):
            adcout|=0x1

    GPIO.output(cspin,True)
    adcout>>=1
    return adcout
#"""********************************************************************""""

#------------------While Loop---------------------------------#
while True:
    adc_val=readadc(1)
    print adc_val
      
   
