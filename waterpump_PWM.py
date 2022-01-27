import RPi.GPIO as GPIO
import time
import pigpio

#make sure you run: sudo pigpiod
#run by using: python3 waterpump_PWM.py
#default values
PWMfreq = 125000
PWMduty = 0
sleepTime = 0.1
rampUpTime = 5

isIncreasing = True

GPIO_PUMP = 13
pi = pigpio.pi()

print("CTRL+C to quit")

#user input PWMfreq
PWMfreq = int(input("Enter PWMfreq: "))
rampUpTime = int(input("Enter ramp up rate (1-10): "))
#scale input rate for more clarity
rampUpTime = rampUpTime * 10000

while True:

    pi.hardware_PWM(GPIO_PUMP, PWMfreq, PWMduty)

    if isIncreasing:
        PWMduty += rampUpTime
    else:
        PWMduty -= rampUpTime

    if PWMduty >= 500000:
        isIncreasing = False

    if PWMduty == 0:
        pi.hardware_PWM(GPIO_PUMP, PWMfreq, PWMduty)
        break;

    time.sleep(sleepTime)







#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(17,GPIO.OUT)
#print ("LED ON")
#GPIO.output(17,GPIO.HIGH)
#time.sleep(15)
#print ("LED OFF")
#GPIO.output(17,GPIO.LOW)
