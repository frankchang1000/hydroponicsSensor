#!/usr/bin/env python3
########################################################################
# Filename    : waterpump_pwm2.py
# Description : Water pump on/off using PWM with sleep timmer

# modification: 2019/3/24
# Confidential and Proprietary
########################################################################
import RPi.GPIO as GPIO
import time
P_PUMP = 18
fPWM = 50
def setup():
    global pwm
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_PUMP, GPIO.OUT)
    pwm = GPIO.PWM(P_PUMP, fPWM)
    pwm.start(0)
print "Starting"
setup()
duty=0
isIncreasing = True
while True:
    pwm.ChangeDutyCycle(duty)
    print "DutyCycle =", duty, "%"
    if isIncreasing:
        duty += 100
    else:
        duty -= 100
    if duty == 100:
        isIncreasing = False
    if duty == 0:
        isIncreasing = True
    time.sleep(5)
            
