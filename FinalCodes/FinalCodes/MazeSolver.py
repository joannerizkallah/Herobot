#This code solves the maze to rescue human at the end of
#the maze using a keep right algorithm
import RPi.GPIO as IO
import time
from Navigate import *
from FuzzyControl import *
from UltrasonicSensor1 import *
from UltrasonicSensor2 import *
from ComplementaryFilter import *

class MazeSolver:
    
    global mpu
    global sensor1
    global sensor2
    global rover
    global fuzzy
    global i
    global direction
    
    #declaring objects for IMU, ultrasonic sensors, navigation of rover, and fuzzy control
    mpu = IMU()
    sensor1 = UltrasonicSensor1()
    sensor2 = UltrasonicSensor2()
    rover = Navigate()
    fuzzy = FuzzyControl()
    
    def init(self):
        IO.setwarnings(False)
        #initializing  IMU and navigation of rover
        mpu.init()
        rover.init()

        #setting pin mode + setting up gpios
        IO.setmode(IO.BCM)

        IO.setup(14,IO.IN) #GPIO 14 -> Right IR out Forward

        IO.setup(15,IO.IN) #GPIO 15 -> Left IR out Forward
        
        IO.setup(5, IO.IN) #GPIO 5 -> Straight Forward
        
        IO.setup(0, IO.IN)# GPIO 0 Straigh Backward
        
        IO.setup(6 ,IO.IN)#GPIO 6 Left Backward
        
        IO.setup(22,IO.IN) #GPIO 22 Right Backward
        
    def solve(self):
        direction = False
        distance = 20
        
        start = time.time()
        while 1:
                
                    
                    #FORWARD 
                    while(IO.input(14)==False and IO.input(5) == True and IO.input(15)==False and direction == True):
                        distance = sensor1.distance()
                        print('distance: ' + str(distance))
                        rover.run('forward')
                        end = time.time()  
                        if end - start >=  mpu.dt:
                            print('forward')
                            start = time.time()
                            end = time.time()
                            mpu.complementaryFilter()
                            print("Pitch: {:.2f}   Roll: {:.2f}   Accel: {:.5f}".format(mpu.getPitch(), mpu.getRoll(), mpu.readAccel()))
                            V =  mpu.readAccel()*mpu.dt
                            print("Velocity : " + str(V))
                            pwm = fuzzy.get_PWM(distance,V)
                            print('pwm' + str(pwm))
                            rover.setPWM(10)
                        if distance < 20:
                         print("Direction flipped")
                         direction = not direction
                            

                        
                    while(IO.input(14)==True and direction == True):
                        
                        rover.setPWM(30)
                        rover.run('right')
                        end = time.time()  
                        if end - start >=  mpu.dt:
                                start = time.time()
                                end = time.time()
                                rover.setPWM(30)
                        
                            
                    while(IO.input(14)==False and IO.input(5)==False and IO.input(15) == True and direction == True):
                        
                        rover.run('left')
                        end = time.time()  
                        if end - start >=  mpu.dt:
                            start = time.time()
                            end = time.time()
                            
                            rover.setPWM(20)
            
                        
                    while(IO.input(14)==False and IO.input(5) == True and IO.input(15)==True  and direction == True):
                        rover.run('forward')
                        distance = sensor1.distance()
                        end = time.time()  
                        if end - start >=  mpu.dt:
                            start = time.time()
                            end = time.time()
                            mpu.complementaryFilter()
                            print("Pitch: {:.2f}   Roll: {:.2f}   Accel: {:.5f}".format(mpu.getPitch(), mpu.getRoll(), mpu.readAccel()))
                            V =  mpu.readAccel()*mpu.dt
                            print("Velocity : " + str(V))
                            pwm = fuzzy.get_PWM(distance,V)
                            rover.setPWM(pwm)
                        if distance < 20:
                            direction = not direction
                            print("Direction flipped: " + str(direction))
                           
                        
                        
                        
                    #REVERSE
                    while(IO.input(22)==False and IO.input(0) == True and IO.input(6)==False and direction == False):
                        
                        distance = sensor2.distance()
                        print('distance' + str(distance))
                        rover.run('reverse')
                        end = time.time()  
                        if end - start >=  mpu.dt:
                            print('reverse')
                            start = time.time()
                            end = time.time()
                            mpu.complementaryFilter()
                            print("Pitch: {:.2f}   Roll: {:.2f}   Accel: {:.5f}".format(mpu.getPitch(), mpu.getRoll(), mpu.readAccel()))
                            V =  mpu.readAccel()*mpu.dt
                            print("Velocity : " + str(V))
                            pwm = fuzzy.get_PWM(distance,V)
                            print('pwm' + str(pwm))
                            rover.setPWM(pwm)
                        if distance < 20:
                            
                            direction = not direction
                            print("Direction flipped: " + str(direction))
                            
                    while(IO.input(22)==True and direction == False):
                        distance = sensor2.distance()
                        rover.setPWM(50)
                        rover.run('reverse left')
                        end = time.time()  
                        if end - start >=  mpu.dt:
                                start = time.time()
                                end = time.time()
                                rover.setPWM(100)
                        if distance < 20:
                            direction = not direction
                            
                    while(IO.input(22)==False and IO.input(0)==False and IO.input(6) == True and direction == False):
                        rover.setPWM(10)
                        distance = sensor2.distance()
                        while(IO.input(0) == False):
                            rover.run('reverse right')
                        distance = sensor2.distance()
                        end = time.time()  
                        if end - start >=  mpu.dt:
                            print('reverse right')
                            start = time.time()
                            end = time.time()
                            rover.setPWM(10)
                        if distance < 10:
                            direction = not direction
                    while(IO.input(22)==False and IO.input(0) == True and IO.input(6)==True  and direction == False):
                        rover.run('reverse')
                        distance = sensor2.distance()
                        end = time.time()  
                        if end - start >=  mpu.dt:
                            print('reverse')
                            
                            start = time.time()
                            end = time.time()
                            mpu.complementaryFilter()
                            print("Pitch: {:.2f}   Roll: {:.2f}   Accel: {:.5f}".format(mpu.getPitch(), mpu.getRoll(), mpu.readAccel()))
                            V =  mpu.readAccel()*mpu.dt
                            print("Velocity : " + str(V))
                            pwm = fuzzy.get_PWM(distance,V)
                            rover.setPWM(pwm)
                        if distance < 20:
                            direction = not direction
                            print("Direction flipped: " + str(direction))
    
            
                
r = MazeSolver()
r.init()
r.solve()
