import os
import sys
import time
import smbus
from math import atan2, sqrt, degrees
from imusensor.MPU9250 import MPU9250
from decimal import Decimal

class IMU:
    global acc
    acc=0
    address = 0x68
    bus = smbus.SMBus(1)
    global imu
    imu= MPU9250.MPU9250(bus, address)
    alpha = 0.98
    dt = 0.01
    pitch = 0
    roll = 0

    @staticmethod
    def init():
        global imu
        imu.begin()
        imu.loadCalibDataFromFile("/home/user/Desktop/Calibration_IMU_Data/Calib.json")

    def readAccel(self):
        global acc
        imu.readSensor()
        imu.computeOrientation()
        Ax = imu.AccelVals[0]
        Ay = imu.AccelVals[1]
        Az = imu.AccelVals[2]
        acc = sqrt(Ax**2 + Ay**2)
        return acc
    
    def readGyro(self):
        imu.readSensor()
        imu.computeOrientation()
        Gx = imu.GyroVals[0]
        Gy = imu.GyroVals[1]
        Gz = imu.GyroVals[2]
        return Gx, Gy, Gz
    
    def complementaryFilter(self):
        Ax, Ay, Az = imu.AccelVals
        Gx, Gy, Gz = self.readGyro()
        
        pitch_acc = atan2(Ax, sqrt(Ay**2 + Az**2))
        roll_acc = atan2(Ay, sqrt(Ax**2 + Az**2))

        pitch_gyro = self.pitch + Gx * self.dt
        roll_gyro = self.roll + Gy * self.dt

        self.pitch = self.alpha * pitch_gyro + (1 - self.alpha) * pitch_acc
        self.roll = self.alpha * roll_gyro + (1 - self.alpha) * roll_acc
    
    def getPitch(self):
        return degrees(self.pitch)
    
    def getRoll(self):
        return degrees(self.roll)

