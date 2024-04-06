import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def fun(channel):
    sleep(0.05)
    while True:
        if GPIO.input(16)== 1:
            print('1')
        else:
            print('0')
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(16,GPIO.RISING,callback=fun)

while True:
    print('principal')
