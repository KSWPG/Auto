import time
import VL53L0X
import RPi.GPIO as GPIO
from DirectionEnum import DirectionEnum as Direction


class SensorsClass:
    def __init__(self):
        self.distanceToCheck = 50 #mm

        self.sensor_front_shutdown = 20
        self.sensor_right_shutdown = 16
        self.sensor_back_shutdown = 21
        self.sensor_left_shutdown = 26

        GPIO.setwarnings(False)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor_front_shutdown, GPIO.OUT)
        GPIO.setup(self.sensor_right_shutdown, GPIO.OUT)
        GPIO.setup(self.sensor_back_shutdown, GPIO.OUT)
        GPIO.setup(self.sensor_left_shutdown, GPIO.OUT)

        GPIO.output(self.sensor_front_shutdown, GPIO.LOW)
        GPIO.output(self.sensor_right_shutdown, GPIO.LOW)
        GPIO.output(self.sensor_back_shutdown, GPIO.LOW)
        GPIO.output(self.sensor_left_shutdown, GPIO.LOW)

        time.sleep(0.50)

        self.tof_front = VL53L0X.VL53L0X(address=0x2B)
        self.tof_right = VL53L0X.VL53L0X(address=0x2D)
        self.tof_back = VL53L0X.VL53L0X(address=0x2A)
        self.tof_left = VL53L0X.VL53L0X(address=0x2C)

        GPIO.output(self.sensor_front_shutdown, GPIO.HIGH)
        time.sleep(0.50)
        self.tof_front.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

        GPIO.output(self.sensor_right_shutdown, GPIO.HIGH)
        time.sleep(0.50)
        self.tof_right.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

        GPIO.output(self.sensor_back_shutdown, GPIO.HIGH)
        time.sleep(0.50)
        self.tof_back.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

        GPIO.output(self.sensor_left_shutdown, GPIO.HIGH)
        time.sleep(0.50)
        self.tof_left.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

    def isWallExist(self, course, direction):
        if ((direction == Direction.MAP_TOP and course == 0) or (direction == Direction.MAP_RIGHT and course == 90) or (direction == Direction.MAP_BOTTOM and course == 180) or (direction == Direction.MAP_LEFT and course == 270)):
            # print("przedni sensorow")
            if(self.tof_front.get_distance() > self.distanceToCheck):
                return False
            else:
                 return True

        elif ((direction == Direction.MAP_RIGHT and course == 0) or (direction == Direction.MAP_TOP and course == 90) or (direction == Direction.MAP_LEFT and course == 180) or (direction == Direction.MAP_BOTTOM and course == 270)):
            # print("prawy sensorow")
            if(self.tof_right.get_distance() > self.distanceToCheck):
                return False
            else:
                return True

        elif ((direction == Direction.MAP_BOTTOM and course == 0) or (direction == Direction.MAP_LEFT and course == 90) or (direction == Direction.MAP_TOP and course == 180) or (direction == Direction.MAP_RIGHT and course == 270)):
            # print("tylni sensorow")
            if(self.tof_back.get_distance() > self.distanceToCheck):
                return False
            else:
                return True

        elif ((direction == Direction.MAP_LEFT and course == 0) or (direction == Direction.MAP_BOTTOM and course == 90) or (direction == Direction.MAP_RIGHT and course == 180) or (direction == Direction.MAP_TOP and course == 270)):
            # print("lewy sensorow")
            if(self.tof_left.get_distance() > self.distanceToCheck):
                return False
            else:
                return True

    def testSensors(self):
        for i in range(0,100):
            print(self.isWallExist(0,Direction.MAP_TOP))
            print(self.isWallExist(90,Direction.MAP_TOP))
            print(self.isWallExist(180,Direction.MAP_TOP))
            print(self.isWallExist(270,Direction.MAP_TOP))
            time.sleep(1)
