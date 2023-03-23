import time
import wiringpi
import sys

def first_blink(groep_1):
    for pin in groep_1:
        wiringpi.digitalWrite(pin, 1)    # Write 1 ( HIGH ) to pin
    time.sleep(1)
    for pin in groep_1:
        wiringpi.digitalWrite(pin, 0)    # Write 1 ( HIGH ) to pin
    time.sleep(1)

def second_blink(groep_2):
    for pin in groep_2:
        wiringpi.digitalWrite(pin, 1)    # Write 1 ( HIGH ) to pin
    time.sleep(1)
    for pin in groep_2:
        wiringpi.digitalWrite(pin, 0)    # Write 1 ( HIGH ) to pin
    time.sleep(1)

#SETUP
print("Start")
groep_1 = [1, 4]
groep_2 =[2, 5]

wiringpi.wiringPiSetup()
for pin in groep_1:
    wiringpi.pinMode(pin, 1)            # Set pin to mode 1 ( OUTPUT )

wiringpi.wiringPiSetup()
for pin in groep_2:
    wiringpi.pinMode(pin, 1)            # Set pin to mode 1 ( OUTPUT )

#MAIN
i = 1
while i == 1:
    first_blink(groep_1)
    second_blink(groep_2)

#cleanup
print("Done")
