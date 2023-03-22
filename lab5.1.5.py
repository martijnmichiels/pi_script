import time
import wiringpi
import sys

def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)    # Write 1 ( HIGH ) to pin
    time.sleep(1)
    wiringpi.digitalWrite(_pin, 0)    # Write 1 ( HIGH ) to pin
    time.sleep(1)


#SETUP
print("Start")
pin12 = [1, 2]
pin34 = [3, 4]

wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)            # Set pin to mode 1 ( OUTPUT )
wiringpi.pinMode(pin2, 1)
wiringpi.pinMode(pin3, 1)
wiringpi.pinMode(pin4, 1)

#MAIN
i = 1
while i == 1:
    blink(pin1.2) 
    blink(pin3.4)

#cleanup
print("Done")