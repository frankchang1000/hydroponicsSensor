#!/usr/bin/env python3
########################################################################
# Filename    : SwitchOverwritePWM.py
# Description : Shutting off light on click and PWM.

# modification: 2019/3/24
# Confidential and Proprietary
########################################################################
import RPi.GPIO as GPIO
import time

ledPin = 18    # define the ledPin(GPIO pin)
buttonPin = 13    # define the buttonPin(GPIO pin)
sleepinterval = 0.8
pressed = 0


def setup():
    print ('Program is starting...')
    GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by GPIO pin, not physical location
    GPIO.setup(ledPin, GPIO.OUT)   # Set ledPin's mode is output
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set buttonPin's mode is input, and pull up to high level(3.3V)
    GPIO.output(ledPin, GPIO.HIGH)

    
def loop():
    pwm = GPIO.PWM(ledPin, 100)    # Created a PWM object
    pwm.start(100)                 # Started PWM at 100% duty cycle
    while True:
        time.sleep(sleepinterval)
        if GPIO.input(buttonPin)==GPIO.HIGH:
            print ('1:led on')  #1 represents high
            GPIO.output(ledPin, GPIO.HIGH)
            pwm.ChangeDutyCycle(100)
            pressed = 0
        else :
            #GPIO.output(ledPin, GPIO.LOW)
            pressed = pressed + 1
            print ('0:User wants to manually dimm off light', pressed)      #0 represents low
            if pressed > 1:
                pressed = 1
            pwm.ChangeDutyCycle(100- pressed*100)
            time.sleep(1)
            
    pwm.stop()      # Stop the PWM
    GPIO.cleanup()  # Make all the output pins LOW

def destroy():
    GPIO.output(ledPin, GPIO.LOW)     # led off
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
