#!/usr/bin/python
import RPi.GPIO as GPIO

class MotorControl:
    def __init__(self,pinDirectionL,pinPWML,pinDirectionR,pinPWMR):
        self.pinDirectionL = pinDirectionL
        self.pinPWML = pinPWML
        self.pinDirectionR = pinDirectionR
        self.pinPWMR = pinPWMR
        self.speedL = 0          #predkosc obrotow lewego silnika w procentach wypelnienia PWM
        self.directionL = 1      #kierunek obrotu lewego silnika 1 jedzie do przodu, -1 jedzie do tylu
        self.speedR = 0         #predkosc obrotow prawego silnika w procentach wypelnienia PWM
        self.directionR = 1     #kierunek obrotu prawego silnika 1 jedzie do przodu, -1 jedzie do tylu

        #przygotowanie koniecznych pinow
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.pinDirectionL, GPIO.OUT)
        GPIO.setup(self.pinPWML, GPIO.OUT)
        GPIO.setup(self.pinDirectionR, GPIO.OUT)
        GPIO.setup(self.pinPWMR, GPIO.OUT)

        #sterowanie kierunkiem
        GPIO.output(self.pinDirectionL, self.directionL)   #kierunek obrotow 1
        GPIO.output(self.pinDirectionR, self.directionR)   #kierunek obrotow 2

        #inicjalizacja pinow PWM
        self.pwmL = GPIO.PWM(self.pinPWML, 50000)     #zdefiniowanie wyscia PWM (PIN_wyjsciowy, czestotliwosc_impulsow)
        self.pwmR = GPIO.PWM(self.pinPWMR, 50000) 			    #aby silnik ruszyl bardzo wazne jest odpowiednie dobranie czestotliwosco impulsow
        self.pwmL.start(0)		    #wysylanie impulsow z wypelnieniem 0%
        self.pwmR.start(0)		    #wysylanie impulsow z wypelnieniem 0%

    def __del__(self):
        GPIO.cleanup()  #zwalnia GPIO dla innych programow

    def showSpeed(self,motor):
        if motor=='L':
            return self.speedL
        else:
            return self.speedR

    def changeSpeed(self,speed,motor='B'):  #zmienia predkosc obrotow silnika na zadany w speed(wartosc wypelnienia impulsow PWM w procentach od 0 do 100), zmiennna motor('L','R') pozwala wybrac silnik, ktorego predkosc obrotow chcemy zmieniec domyslnie zmienia dla obu
        if(0<=speed && 100>=speed):
            if motor=='L':
                self.speedL = speed
                self.pwmL.ChangeDutyCycle(speed)    #zmienia wartosc wypelnienia impulsow PWM
            elif motor=='R':
                self.speedR = speed
                self.pwmR.ChangeDutyCycle(speed)
            else:
                self.speedL = speed
                self.speedR = speed

                self.pwmL.ChangeDutyCycle(speed)
                self.pwmR.ChangeDutyCycle(speed)

    def showDirection(self,motor):
        if motor=='L':
            return self.DirectionL
        else:
            return self.DirectionR

    def changeDirection(self,newDirection,motor='B'):       #zmienia kierunek obrotu silnika na zadany w newDirection(-1,1), zmienna motor('L','R') pozwala wybrac silnik, ktorego kierunek obrotow chcemy zmieniec domyslnie zmienia dla obu
        if(newDirection==-1 || newDirection==1):
            if motor=='L':
                self.changeSpeed(0,'L')
                self.DirectionL = newDirection
                if newDirection == -1:
                    newDirection = 0
                GPIO.output(self.pinDirectionL, newDirection)
            elif motor=='R':
                self.changeSpeed(0,'R')
                self.DirectionR = newDirection
                if newDirection == -1:
                    newDirection = 0
                GPIO.output(self.pinDirectionR, newDirection)
            else:
                self.changeSpeed(0)
                self.DirectionL = newDirection
                self.DirectionR = newDirection

                if newDirection == -1:
                    newDirection = 0
                GPIO.output(self.pinDirectionL, newDirection)
                GPIO.output(self.pinDirectionR, newDirection)

    def turn(self,direction,difference=10):     #pozwala na skret w lewo lub prawo w zaleznosci od zmiennej direction('L','R') poprzez zmiane wartosci predkosci silnikow o zadana w zmiennej difference
        speedL = 0
        speedR = 0

        if direction == 'L':
            speedL = self.speedL - difference
            if speedL < 0 : speedL = 0
            speedR = self.speedR + difference
            if speedR > 100 : speedR = 100

        if direction == 'R':
            speedL = self.speedL + difference
            if speedL > 100 : speedL = 100
            speedR = self.speedR - difference
            if speedR < 0 : speedR = 0

        self.changeSpeed(speedL,'L')
        self.changeSpeed(speedR,'R')

    def straight(self):     #ustawia predkosc obu silnikow na wartosc sredniej arytmetycznej ich wczesniejszych predkosci
        newSpeed = (self.speedL+self.speedR)/2;
        self.changeSpeed(newSpeed)

    def rotateInPoint(self,speed,direction):    #pozwala na obrot w miejscu z predkosci zadana w zmiennej speed(wartosc wypelnienia impulsow PWM w procentach od 0 do 100) i w kierunku zadanym przez zmienna direction
        if(0<=speed && 100>=speed):
            if direction == 'R':
                self.changeDirection(1,'L')
                self.changeDirection(-1,'R')
            else:
                self.changeDirection(-1,'L')
                self.changeDirection(1,'R')

            self.changeSpeed(speed)
