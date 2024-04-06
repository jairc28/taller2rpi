import RPi.GPIO as GPIO
from time import sleep

bit1=11
bit2=13
bit3=15
bit4=29

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(bit1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(bit2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(bit3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(bit4,GPIO.OUT,initial=GPIO.LOW)

def vuelta():
    #paso1 
    GPIO.output(bit1,GPIO.HIGH) #1
    GPIO.output(bit2,GPIO.LOW) #0
    GPIO.output(bit3,GPIO.LOW) #0
    GPIO.output(bit4,GPIO.LOW) #0
    sleep(0.01)
    #paso2
    GPIO.output(bit1,GPIO.HIGH) #1
    GPIO.output(bit2,GPIO.HIGH) #1
    GPIO.output(bit3,GPIO.LOW) #0
    GPIO.output(bit4,GPIO.LOW) #0
    sleep(0.01)
    #paso3
    GPIO.output(bit1,GPIO.LOW) #0
    GPIO.output(bit2,GPIO.HIGH) #1
    GPIO.output(bit3,GPIO.LOW) #0
    GPIO.output(bit4,GPIO.LOW) #0
    sleep(0.01)
    #paso4
    GPIO.output(bit1,GPIO.LOW) #0
    GPIO.output(bit2,GPIO.HIGH) #1
    GPIO.output(bit3,GPIO.HIGH) #1
    GPIO.output(bit4,GPIO.LOW) #0
    sleep(0.01)
    #paso5
    GPIO.output(bit1,GPIO.LOW) #0
    GPIO.output(bit2,GPIO.LOW) #0
    GPIO.output(bit3,GPIO.HIGH) #1
    GPIO.output(bit4,GPIO.LOW) #0
    sleep(0.01)
    #paso6
    GPIO.output(bit1,GPIO.LOW) #0
    GPIO.output(bit2,GPIO.LOW) #0
    GPIO.output(bit3,GPIO.HIGH) #1
    GPIO.output(bit4,GPIO.HIGH) #1
    sleep(0.01)
    #paso7
    GPIO.output(bit1,GPIO.LOW) #0
    GPIO.output(bit2,GPIO.LOW) #0
    GPIO.output(bit3,GPIO.LOW) #0
    GPIO.output(bit4,GPIO.HIGH) #1
    sleep(0.01)
    #paso8
    GPIO.output(bit1,GPIO.LOW) #1
    GPIO.output(bit2,GPIO.LOW) #0
    GPIO.output(bit3,GPIO.LOW) #0
    GPIO.output(bit4,GPIO.HIGH) #1
    sleep(0.01)



for i in range (512):
    vuelta()
    sleep(0.01)