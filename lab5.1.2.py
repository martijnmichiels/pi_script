import time
import wiringpi
import sys

def blink(pins):
    for pin in pins:
        wiringpi.digitalWrite(pin, 1)    # Write 1 ( HIGH ) to pin
    time.sleep(0.1)
    for pin in pins:
        wiringpi.digitalWrite(pin, 0)    # Write 1 ( HIGH ) to pin
    time.sleep(0.1)

#SETUP
print("Start")
pins = [1, 2, 4, 5]

wiringpi.wiringPiSetup()
for pin in pins:
    wiringpi.pinMode(pin, 1)            # Set pin to mode 1 ( OUTPUT )

#MAIN
i = 1
while i == 1:
    blink(pins)

#cleanup
print("Done")
