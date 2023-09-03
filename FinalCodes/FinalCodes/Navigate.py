import RPi.GPIO as GPIO
import time
from time import sleep

class Navigate:
    global inB1
    inB1 = 21
    global inB2
    inB2 = 23
    global inB3
    inB3= 27
    global inB4
    inB4=8
    global inF1
    inF1 = 20
    global inF2
    inF2 = 16
    global inF3
    inF3= 26
    global inF4
    inF4=4
    global enB1
    enB1 = 13
    global enB2
    enB2= 19
    global enF1
    enF1 = 18
    global enF2
    enF2= 12
    global p
    global p2
    global p3
    global p4
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(enB1,GPIO.OUT)
    GPIO.setup(enB2,GPIO.OUT)
    GPIO.setup(enF1,GPIO.OUT)
    GPIO.setup(enF2,GPIO.OUT)
    p=GPIO.PWM(enB1,100)
    p2=GPIO.PWM(enB2,100)
    p3=GPIO.PWM(enF1,100)
    p4=GPIO.PWM(enF2,100)
    
    @staticmethod
    def init():
        
        GPIO.setup(inB1,GPIO.OUT)
        GPIO.setup(inB2,GPIO.OUT)
        GPIO.output(inB1,GPIO.LOW)
        GPIO.output(inB2,GPIO.LOW)
        GPIO.setup(inB3,GPIO.OUT)
        GPIO.setup(inB4,GPIO.OUT)
        GPIO.output(inB3,GPIO.LOW)
        GPIO.output(inB4,GPIO.LOW)
        GPIO.setup(inF1,GPIO.OUT)
        GPIO.setup(inF2,GPIO.OUT)
        GPIO.output(inF1,GPIO.LOW)
        GPIO.output(inF2,GPIO.LOW)
        GPIO.setup(inF3,GPIO.OUT)
        GPIO.setup(inF4,GPIO.OUT)
        GPIO.output(inF3,GPIO.LOW)
        GPIO.output(inF4,GPIO.LOW)
        
        
    def setPWM(self, PWM):
        p.start(PWM)
        p2.start(PWM)
        p3.start(PWM)
        p4.start(PWM)
        
    def setPWM_LEFT(self, PWM):
        p.start(PWM)
        p4.start(PWM)
        
    def setPWM_RIGHT(self, PWM):
        p2.start(PWM)
        p3.start(PWM)
        
    def run(self, y):
        start = time.time()
        x = y
        if x=='forward':
            print("forward")
            GPIO.output(inB1,GPIO.LOW)
            GPIO.output(inB2,GPIO.HIGH)
            GPIO.output(inB3,GPIO.HIGH)
            GPIO.output(inB4,GPIO.LOW)
            GPIO.output(inF1,GPIO.HIGH)
            GPIO.output(inF2,GPIO.LOW)
            GPIO.output(inF3,GPIO.HIGH)
            GPIO.output(inF4,GPIO.LOW)  
            y = 'forward'
                    
        elif x=='reverse':
            print('reverse')
            GPIO.output(inB1,GPIO.HIGH)
            GPIO.output(inB2,GPIO.LOW)
            GPIO.output(inB3,GPIO.LOW)
            GPIO.output(inB4,GPIO.HIGH)
            GPIO.output(inF1,GPIO.LOW)
            GPIO.output(inF2,GPIO.HIGH)
            GPIO.output(inF3,GPIO.LOW)
            GPIO.output(inF4,GPIO.HIGH)
            y = 'reverse'
            
        elif x=='stop':
            print("stop")
            GPIO.output(inF1, GPIO.LOW)
            GPIO.output(inF2, GPIO.LOW)
            GPIO.output(inF3, GPIO.LOW)
            GPIO.output(inF4, GPIO.LOW)
            GPIO.output(inB1, GPIO.LOW)
            GPIO.output(inB2, GPIO.LOW)
            GPIO.output(inB3, GPIO.LOW)
            GPIO.output(inB4, GPIO.LOW)
            y = 'stop'    
                
        elif x=='left':
            print("turn left")
            #turn on right side 
            GPIO.output(inF1,GPIO.HIGH)
            GPIO.output(inF2,GPIO.LOW)
            GPIO.output(inB3,GPIO.HIGH)
            GPIO.output(inB4,GPIO.LOW)
            #turn off left side
            GPIO.output(inF3,GPIO.LOW)
            GPIO.output(inF4,GPIO.LOW)
            GPIO.output(inB1,GPIO.LOW)
            GPIO.output(inB2,GPIO.LOW)
            y = 'left'
        elif x=='reverse left':
            print("reverse left")
            #turn on right side 
            GPIO.output(inF1,GPIO.LOW)
            GPIO.output(inF2,GPIO.HIGH)
            GPIO.output(inB3,GPIO.LOW)
            GPIO.output(inB4,GPIO.HIGH)
            #turn off left side
            GPIO.output(inF3,GPIO.LOW)
            GPIO.output(inF4,GPIO.LOW)
            GPIO.output(inB1,GPIO.LOW)
            GPIO.output(inB2,GPIO.LOW)
            y = 'reverse left'
                        
        elif x=='right':
            print("turn right")
            #turn off right side 
            GPIO.output(inF1,GPIO.LOW)
            GPIO.output(inF2,GPIO.LOW)
            GPIO.output(inB3,GPIO.LOW)
            GPIO.output(inB4,GPIO.LOW)
            #turn on left side
            GPIO.output(inF3,GPIO.HIGH)
            GPIO.output(inF4,GPIO.LOW)
            GPIO.output(inB2,GPIO.HIGH)
            GPIO.output(inB1,GPIO.LOW)
            y = 'right'
        
        elif x=='reverse right':
            print("reverse right")
            #turn off right side 
            GPIO.output(inF1,GPIO.LOW)
            GPIO.output(inF2,GPIO.LOW)
            GPIO.output(inB3,GPIO.LOW)
            GPIO.output(inB4,GPIO.LOW)
            #turn on left side
            GPIO.output(inF3,GPIO.LOW)
            GPIO.output(inF4,GPIO.HIGH)
            GPIO.output(inB2,GPIO.LOW)
            GPIO.output(inB1,GPIO.HIGH)
            y = 'reverse right'
        
        
        else:
            print("<<<  wrong data  >>>")
            print("please enter the a valid direction to continue.....")
