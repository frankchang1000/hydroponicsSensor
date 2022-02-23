import RPi.GPIO as GPIO
import time

P_LED = 12
fPWM = 10000

def setup():
	global pwm
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(P_LED, GPIO.OUT)
	pwm = GPIO.PWM(P_LED, fPWM)
	pwm.start(0)

print "Starting"
setup()
duty=0
isIncreasing = True
while True:
	pwm.ChangeDutyCycle(duty)
	print "DutyCycle =", duty, "%"
	if isIncreasing:
		duty += 25
	else:
		duty -= 25
	if duty == 25:
		isIncreasing = True
	if duty == 0:
		isIncreasing = False
	time.sleep(10)
			
