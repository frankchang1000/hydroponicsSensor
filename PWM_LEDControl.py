import RPi.GPIO as GPIO
import time
import pigpio

#make sure you run: sudo pigpiod
#run by using: python3 PWM_LEDControl.py
#default values
PWMfreq = 125000
PWMduty = 0
sleepTime = 0.1

isIncreasing = True

GPIO_LED = 18
GPIO_EN_LED = 17
pi = pigpio.pi()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GPIO_EN_LED,GPIO.OUT)

#EN_LED on or off
EN_onoff = int(input("Enter EN_LED 0 or 1: "))
if EN_onoff == 0:
    GPIO.output(GPIO_EN_LED,GPIO.LOW)

else:
    GPIO.output(GPIO_EN_LED,GPIO.HIGH)

print("CTRL+C to quit")

while True:

    EN_LED = GPIO.input(GPIO_EN_LED)

    pi.hardware_PWM(18, PWMfreq, PWMduty)

    if isIncreasing:
        PWMduty += 10000
    else:
        PWMduty -= 10000

    if PWMduty >= 1000000:
        isIncreasing = False

    if PWMduty == 0:
        pi.hardware_PWM(GPIO_LED, PWMfreq, PWMduty)
        break;

    time.sleep(sleepTime)
    #check if EN_LED is high
    if EN_LED:
        #print("EN_LED is ON, PWMfreq: ", PWMfreq, ", PWMduty: ", PWMduty)
        #always check for new PWMfreq and PWMduty from user
        pi.hardware_PWM(GPIO_LED, PWMfreq, PWMduty)
    else:
        #print("EN_LED is OFF, PWMfreq: 0, PWMduty: 0")
        pi.hardware_PWM(GPIO_LED,0,0)

GPIO.output(GPIO_EN_LED,GPIO.LOW)







#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(17,GPIO.OUT)
#print ("LED ON")
#GPIO.output(17,GPIO.HIGH)
#time.sleep(15)
#print ("LED OFF")
#GPIO.output(17,GPIO.LOW)
