import os
import sys
import time
import smbus
import numpy as np

from imusensor.MPU9250 import MPU9250

address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()
imu.caliberateAccelerometer()
print ("Acceleration calib successful")

print ("Mag calib successful")

accelscale = imu.Accels
accelBias = imu.AccelBias
gyroBias = imu.GyroBias


imu.saveCalibDataToFile("/home/user/Desktop/Calibration_IMU_Data/Calib.json")
print ("calib data saved")

imu.loadCalibDataFromFile("/home/user/Desktop/Calibration_IMU_Data/Calib.json")
if np.array_equal(accelscale, imu.Accels) & np.array_equal(accelBias, imu.AccelBias) & \
	np.array_equal(gyroBias, imu.GyroBias):
	print ("calib loaded properly")
