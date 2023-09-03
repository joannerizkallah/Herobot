#This code is used to tes cruise control
import RPi.GPIO as IO
import time
import csv
from Navigate import *
from UltrasonicSensor1 import *
from FuzzyControl import *
from FuzzyControl import *
from ComplementaryFilter import *

#declaring and initializing all objects
mpu = IMU()
mpu.init()
rover = Navigate()
rover.init()
sensor1 = UltrasonicSensor1()
fuzzy = FuzzyControl()
start = time.time()
while 1:
    with open('accNEW.csv', 'a') as file: 
        distance = sensor1.distance()
        print('Distance: ' + str(distance))
        end = time.time()
        if end - start >=  mpu.dt:
                print('forward')
                start = time.time()
                end = time.time()
                mpu.complementaryFilter()
                file.write(str(mpu.readAccel()) + "\n")
                print("Pitch: {:.2f}   Roll: {:.2f}   Accel: {:.5f}".format(mpu.getPitch(), mpu.getRoll(), mpu.readAccel()))
                V =  mpu.readAccel()*mpu.dt
                print("Velocity : " + str(V))
                pwm = fuzzy.get_PWM(distance,V)
                print('pwm: ' + str(pwm))
                rover.setPWM(pwm)
                rover.run('forward')
