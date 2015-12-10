"""***********************************************************************
Author      : 
Organization:  Emnics Technologies Pvt Ltd
Description :  Sample code for all the available GPIOs in ESCUDO
***********************************************************************"""


import RPi.GPIO as GPIO              # Importing RPi.GPIO library
from time import sleep               # Importing Delay Library
GPIO.setmode(GPIO.BOARD)             # seting GPIO Pin number selection based on board Pin no

GPIO.setwarnings(False)              # Set the warning false to reuse the GPIO

RELAY = [7,11,12,13,15,16,18,24]     # Pin nos of the relays in ESCUDO connected to Raspberry Pi

LED = [29]                           # On board LED Pin No

BUZZER = [22]                        #Escudo Buzzer Pin No

INPUTS=[40,37,38,35,36,33,31,32]

#----set the direction of Relays, Buzzer and LED as output-----#
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
#---------------------------------------------------------------#


#--set the direction of ESCUDO Opto Isolated input pin as Input-#
GPIO.setup(40,GPIO.IN)
GPIO.setup(37,GPIO.IN)
GPIO.setup(38,GPIO.IN)
GPIO.setup(35,GPIO.IN)
GPIO.setup(36,GPIO.IN)
GPIO.setup(33,GPIO.IN)
GPIO.setup(31,GPIO.IN)
GPIO.setup(32,GPIO.IN)
#----------------------------------------------------------------#

#-------------Set all outputs to Low/False-----------------------#

#GPIO.output(BUZZER[0],False)

GPIO.output(RELAY[0],False)
GPIO.output(RELAY[1],False)
GPIO.output(RELAY[2],False)
GPIO.output(RELAY[3],False)
GPIO.output(RELAY[4],False)
GPIO.output(RELAY[5],False)
GPIO.output(RELAY[6],False)
GPIO.output(RELAY[7],False)
#------------------------------------------------------------------#

#---------------Entering while loop---------------------------------#
while(1):

    #----monitoring GPIO input pin continously------------#
    if(GPIO.input(INPUTS[0])==0):
       GPIO.output(RELAY[7],True)        # setting Relay 8(RELAY[7] true if Input 1 is low
       print "sw on"
    else:
        GPIO.output(RELAY[7],False)       # setting Relay 8(RELAY[7]  False if Input 1 is low
        print "sw off"
    
    #-- samilarly all th IOs can be used based on application-----#
