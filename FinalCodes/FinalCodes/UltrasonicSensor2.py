import RPi.GPIO as GPIO
import time
class UltrasonicSensor2:
    #GPIO Mode (BOARD / BCM)
    
    GPIO.cleanup() 
    global TRIGGER
    TRIGGER = 17
    global ECHO
    ECHO = 25
    #set GPIO direction (IN / OUT)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIGGER, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    global maxTime
    maxTime = 0.4
    @staticmethod
    def distance():
        # set Trigger to HIGH
        GPIO.output(TRIGGER, True)
     
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(TRIGGER, False)
     
        StartTime = time.time()
        StopTime = time.time()
        timeout = maxTime + StartTime 
        # save StartTime
        while GPIO.input(ECHO) == 0 and StartTime < timeout:
            StartTime = time.time()
            
     
        # save time of arrival
        while GPIO.input(ECHO) == 1 and StartTime< timeout:
            StopTime = time.time()
     
            # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
     
        return distance




