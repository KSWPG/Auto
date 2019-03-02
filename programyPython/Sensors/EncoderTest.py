import time
import RPi.GPIO as GPIO

PIN_NUMBER = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NUMBER, GPIO.IN)

for i in range(0,100):
    print(GPIO.input(PIN_NUMBER))
    time.sleep(1)
