import RPi.GPIO as GPIO
from time import sleep
import os
import smbus
bus=smbus.SMBus(1)
GPIO.setmode(GPIO.BCM)

DEBUG=1


#---------------ADC read Function definition--------------------#
#function Name        : readadc
#arguments            : ADC number,SPI clock pin no,MOSI,MISO,CS pin nos
#return                : adc value
#---------------------------------------------------------------#
def readadc(adcnum,clockpin,mosipin,misopin,cspin):
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
#------------------------------------------------------------#
#-----------------SPI Pin Nos--------------------------------#
SPICLK=11
SPIMOSI=10
SPIMISO=9
SPICS=7
#------------------------------------------------------------#
#---------------------SPI PIN DIRECTIONS---------------------#
GPIO.setup(SPIMOSI,GPIO.OUT)
GPIO.setup(SPIMISO,GPIO.IN)
GPIO.setup(SPICLK,GPIO.OUT)
GPIO.setup(SPICS,GPIO.OUT)
#------------------------------------------------------------#

#---------------------Initialisation-------------------------#
potentiometer_adc=7           #ADC No           
last_read=0                   # To store Last read ADC value
tolerance=5                   # Tolerance variable (Modifiable)
#------------------------------------------------------------#

#------------------While Loop---------------------------------#
while True:
    trim_pot_changed=False
    trim_pot=readadc(potentiometer_adc,SPICLK,SPIMOSI,SPIMISO,SPICS)
    pot_adjust=abs(trim_pot-last_read)          # To adjust ADC val to zero if tolernance exist
    voltage=(trim_pot*3300)/1024                # ADC volatge
    print voltage
        
    if(pot_adjust>tolerance):
        trim_pot_changed=True

    if(trim_pot_changed):                      # if diff btw adc val and last read value is greater than
        set_volume=trim_pot/10.24              # tolerance
        set_volume=round(set_volume)
        set_volume=int(set_volume)
       
    last_read=trim_pot

   
