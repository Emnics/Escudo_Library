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
    global Flag
    input_no=input_no-1
    if((input_no>7) or (input_no<0)):
        print("please rnter correct input noumber between 1 to 8")
        Flag=1
        return 
    if(GPIO.input(INPUT[input_no])==0):
       input_data=0
    else:
       input_data=1
    return input_data
#"""********************************************************************""""

#"""*********************************************************************"""
#Function Name   :readadc(adcnum)
#Descriptions    :reads corresponding ADC inputs and return ADC value
#Argument        :adcnum (adc number between 1 to 8)
#Return          :adc output vale (eg 0 to 1023)
"***********************************************************************"""

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
"""LED_ON()
Turn_ON_Buzzer()
sleep(0.5)
Turn_OFF_Buzzer()
LED_OFF()"""
#sleep(1)
Set_Time(14,30,0)
#Save_To_Memory(2,10)
while(1):
     #x=Read_From_Memory(2)
     #print x
     x=readadc(3)
     print x
     #sleep(1)
     #time=Read_Time()
     #print time
     sleep(1)
     if(0==Read_Input(3)):
            print "sw ON"
            Turn_ON_Relay(3)
     else:
            print  "sw off"
            Turn_OFF_Relay(3)
