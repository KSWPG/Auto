from Package import MotorControl
from time import sleep
import RPi.GPIO as GPIO


################################# INICJALIZACJA ############################
############################################################################




################################# CZUJNIKI #################################
############################################################################





################################ ALGORYTM #################################
############################### MAPOWANIA #################################




################################ SILNIKI ##################################
############################################################################


GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.output(4, GPIO.LOW)
#test = MotorControl(12,20,21,16)
test = MotorControl(23,12,22,13)
test.changeSpeed(50)
sleep(2)
test.turn('L',50)
sleep(2)
test.straight()
sleep(0.5)
test.turn('R',50)
sleep(2)
test.straight()
sleep(1)
test.turn('L')
sleep(2)
test.rotateInPoint(50,"R")
sleep(2)
test.rotateInPoint(50,"L")
sleep(2)

GPIO.cleanup()
