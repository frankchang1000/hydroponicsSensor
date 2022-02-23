import pigpio
import time
pi = pigpio.pi()
pi.set_PWM_frequency(18, 125000)
duty=0
isIncreasing = True

while True:
    pi.set_PWM_dutycycle(18, duty)
    
    if isIncreasing:
        duty += 1
    else:
        duty -= 1

    if duty == 255:
        isIncreasing = False
        
    if duty == 0:
        pi.set_PWM_dutycycle(18, duty)
        break;
    
    time.sleep(.1)
            

pi.stop()