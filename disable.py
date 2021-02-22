import RPi.GPIO as GPIO
from time import sleep
  
# here you would put all your code for setting up GPIO,  
# we'll cover that tomorrow  
# initial values of variables etc...  
counter = 0

# per https://www.rototron.info/raspberry-pi-stepper-motor-tutorial/
EN = 16    # Enable GPIO Pin
  
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN, GPIO.OUT)
GPIO.output(DIR, CW)

try:  
    # here you put your main loop or block of code  
    #while counter < 9000000:  
    #    # count up to 9000000 - takes ~20s  
    #    counter += 1  
    #print("Target reached: %d" % counter)
        
    print("Disabling the driver...")
    GPIO.output(EN, GPIO.HIGH)

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print("\n", counter) # print value of counter  
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print("Other error or exception occurred!")  
  
finally:  
    GPIO.cleanup() # this ensures a clean exit  