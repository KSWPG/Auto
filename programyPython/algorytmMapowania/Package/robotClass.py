import numpy as np
#import RPi.GPIO as GPIO

#from Package import MotorControl
from mapMatrixClass import mapMatrixClass
from simulationMapMatrixClass import simulationMapMatrixClass


class robotClass:
	def __init__(self):
		#GPIO.setmode(GPIO.BCM)

		#inicjalizacja silnikow
		#self.motors = MotorControl(23,12,22,13)

		#inicjalizacja sensorow
		#/########################

		#wykorzystwane tylko do testowania algorytmu potem do usuniecia
		self.simulationMap = simulationMapMatrixClass(10,10)
		self.simulationMap.prepareTable()

		self.course = 0
		self.x = 0
		self.y = 0

		self.moves=0

		self.map = mapMatrixClass(1,1)

	def addToCourse(self, angle):
		if ((angle == 90) or (angle == 180) or (angle == 270)):
			course = self.course + angle
			if course < 360: self.course = course
			elif course == 360: self.course = 0
			elif course == 450: self.course = 90
			elif course == 540: self.course = 180
		else:
			 raise Exception('The value of the angle should be 90,180 or 270.')

	def checkSensor(self):
		#do testow, pozniej do zamienia przez odczyty z czujnikow ktory bedzie trzeba uzaleznic od wartosci self.course
		if self.simulationMap.isWallExist(self.x,self.y,"N"):
			self.map.setWallsInContiguousField(self.x,self.y,"N")
		elif self.map.addNewRowIfNeeded(self.y,"N"):
			pass

		if self.simulationMap.isWallExist(self.x,self.y,"E"):
			self.map.setWallsInContiguousField(self.x,self.y,"E")
		elif self.map.addNewColumnIfNeeded(self.x,"E"):
			pass

		if self.simulationMap.isWallExist(self.x,self.y,"S"):
			self.map.setWallsInContiguousField(self.x,self.y,"S")
		elif self.map.addNewRowIfNeeded(self.y,"S"):
			self.y = self.y + 1

		if self.simulationMap.isWallExist(self.x,self.y,"W"):
			self.map.setWallsInContiguousField(self.x,self.y,"W")
		elif self.map.addNewColumnIfNeeded(self.x,"W"):
			self.x = self.x +1

		self.map.setVisited(self.x,self.y)

	def goForward(self):
		#motors.ForwardOneField
		if self.course == 0: self.y = self.y + 1
		elif self.course == 90: self.x = self.x + 1
		elif self.course == 180: self.y = self.y - 1
		elif self.course == 270: self.x = self.x - 1

	def goRight(self):
		#motors.turnRight
		self.addToCourse(90)
		self.goForward()

	def goBack(self):
		#motors.turnBack
		self.addToCourse(180)
		self.goForward()

	def goLeft(self):
		#motors.turnLeft
		self.addToCourse(270)
		self.goForward()

	def goByPath(self,pathMap):
		while (pathMap[self.x][self.y] != 1):
			actualValue = pathMap[self.x][self.y]
			if(self.x != self.map.xSize-1 and pathMap[self.x+1][self.y] == actualValue-1):
				if self.course == 0:
					self.goRight()
				elif self.course == 90:
					self.goForward()
				elif self.course == 180:
					self.goLeft()
				elif self.course == 270:
					self.goBack()
			elif(self.x != 0 and pathMap[self.x-1][self.y] == actualValue-1):
				if self.course == 0:
					self.goLeft()
				elif self.course == 90:
					self.goBack()
				elif self.course == 180:
					self.goRight()
				elif self.course == 270:
					self.goForward()
			elif(self.y != self.map.ySize-1 and pathMap[self.x][self.y+1] == actualValue-1):
				if self.course == 0:
					self.goForward()
				elif self.course == 90:
					self.goLeft()
				elif self.course == 180:
					self.goBack()
				elif self.course == 270:
					self.goRight()
			elif(self.y != 0 and pathMap[self.x][self.y-1] == actualValue-1):
				if self.course == 0:
					self.goBack()
				elif self.course == 90:
					self.goRight()
				elif self.course == 180:
					self.goForward()
				elif self.course == 270:
					self.goLeft()

			self.moves=self.moves+1
