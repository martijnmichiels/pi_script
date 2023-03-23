import time
import wiringpi
import sys

def shortblink(short):
    for pin in groep_1:
        wiringpi.digitalWrite(pin, 1)    # Write 1 ( HIGH ) to pin
    time.sleep(0.5)
    for pin in groep_1:
        wiringpi.digitalWrite(pin, 0)    # Write 1 ( HIGH ) to pin
    time.sleep(0.5)

def longblink(long):
    for pin in groep_1:
        wiringpi.digitalWrite(pin, 1)    # Write 1 ( HIGH ) to pin
    time.sleep(1.5)
    for pin in groep_1:
        wiringpi.digitalWrite(pin, 0)    # Write 1 ( HIGH ) to pin
    time.sleep(1.5)

    #SETUP
print("Start")
groep_1 = [1, 2, 3, 4]

wiringpi.wiringPiSetup()
for pin in groep_1:
    wiringpi.pinMode(pin, 1)            # Set pin to mode 1 ( OUTPUT )

    #MAIN
i = 1
while i == 1:
    first_blink(groep_1)

#cleanup
print("Done")