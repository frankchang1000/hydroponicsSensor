import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT)
print "Pump ON"
GPIO.output(24,GPIO.HIGH)
time.sleep(15)
print "Pump OFF"
GPIO.output(24,GPIO.LOW)
