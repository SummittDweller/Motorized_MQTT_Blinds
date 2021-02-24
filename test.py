import RPi.GPIO as GPIO
from time import sleep
  
# here you would put all your code for setting up GPIO 

# per https://www.rototron.info/raspberry-pi-stepper-motor-tutorial w/ pin
# modifications so that all 4 RPi pins are clustered in one corner/connector
DIR = 21    # Direction GPIO Pin
STEP = 20   # Step GPIO Pin
CW = 1      # Clockwise Rotation
CCW = 0     # Counterclockwise Rotation
SPR = 2038  # Steps per Revolution per https://mschoeffler.com/2017/09/23/tutorial-how-to-drive-the-28byj-48-stepper-motor-with-a-uln2003a-driver-board-and-an-arduino-uno/
EN = 16     # Enable GPIO Pin
  
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)
GPIO.output(DIR, CW)

do_return = True
step_count = int(SPR / 1)   # for fraction of one rotation 
delay = .0005    # was .0208 but this is much faster and smoother without overheating
  
try:  
    # here you put your main loop or block of code  
    #while counter < 9000000:  
    #    # count up to 9000000 - takes ~20s  
    #    counter += 1  
    #print("Target reached: %d" % counter)
    
    print("Enabling the driver...")
    GPIO.output(EN, GPIO.LOW)
    
    print("Rotating CW for %d steps..." % step_count)
    for x in range(step_count):
      GPIO.output(STEP, GPIO.HIGH)
      sleep(delay)
      GPIO.output(STEP, GPIO.LOW)
      sleep(delay)
    print("Completed %d steps CW rotation." % step_count)
 
 
    if do_return:
      sleep(.5)
      GPIO.output(DIR, CCW)
    
      print("Rotating CCW for %d steps..." % step_count)
      for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
      print("Completed %d steps CCW rotation." % step_count)
    
    print("Disabling the driver...")
    GPIO.output(EN, GPIO.HIGH)

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C
    print("Keyboard interrupt...disabling the driver...")
    GPIO.output(EN, GPIO.HIGH)
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print("Other error or exception occurred!")  
  
finally:  
    GPIO.cleanup() # this ensures a clean exit
    print("Done.")