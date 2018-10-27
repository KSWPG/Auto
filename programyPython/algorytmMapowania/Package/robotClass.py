import numpy as np
import RPi.GPIO as GPIO

#from Package import MotorControl
from mapMatrixClass import mapMatrixClass

class robotClass:
	def __init__(self):
		#GPIO.setmode(GPIO.BCM)
		
		#inicjalizacja silnikow
		#motors = MotorControl(23,12,22,13)
		
		#inicjalizacja sensorow
		#/########################
		
		#wykorzystwane tylko do testowania algorytmu potem do usuniecia
		self.simulationMap = mapMatrixClass(10,10)		
		self.simulationMap.prepareTable()
		self.course = 0
		self.setRobotPosition()
		#okreslenie pola poczatkowego
		self.startX = 0
		self.startY = 0
		
		self.x = self.startX
		self.y = self.startY
		#inicjalizacja mapy
		self.map = mapMatrixClass(10,10)
	
	def setRobotPosition(self):
		return True
		#ustawic tak robota zeby jego lewy czujnik dotykal krawedz pomieszczenia i tak zmien self.course zeby zgadzalo sie z polozeniem robota
		
	def setCourse(self, angle):  #dodaje do obecnego kierunku zadana wartosc
		if ((angle == 90) or (angle == 180) or (angle == 270)):
			course = self.course + angle
			if course < 360: self.course = course
			elif course == 360: self.course = 0
			elif course == 450: self.course = 90
			elif course == 540: self.course = 180
		
	def checkSensor(self):
		#do testow, pozniej do zamienia przez odczyty z czujnikow ktory bedzie trzeba uzaleznic od wartosci self.course
		if self.simulationMap.isWallExist(self.x,self.y,"N"): 
			self.map.setSolidWall(self.x,self.y,"N")
			if self.y !=9 : self.map.setSolidWall(self.x,self.y+1,"S")
		if self.simulationMap.isWallExist(self.x,self.y,"E"): 
			self.map.setSolidWall(self.x,self.y,"E")
			if self.x !=9 : self.map.setSolidWall(self.x+1,self.y,"W")
		if self.simulationMap.isWallExist(self.x,self.y,"S"): 
			self.map.setSolidWall(self.x,self.y,"S")
			if self.y !=0 : self.map.setSolidWall(self.x,self.y-1,"N")
		if self.simulationMap.isWallExist(self.x,self.y,"W"): 
			self.map.setSolidWall(self.x,self.y,"W")
			if self.x !=0 : self.map.setSolidWall(self.x-1,self.y,"E")
		self.map.setVisited(self.x,self.y)
		
	def go(self,direction = "F"):
		if direction == "F":
			#we wlaciwym kodzie tylko porusz sie za pomoca silnikow o jedno pole course
			self.setCourse(0)
		elif direction == "R":
			#we wlasiciwym kodzie obroc sie w prawo i porusz o jedno pole zmien wartosc course o +90
			self.setCourse(90)
		elif direction == "B":
			#we wlasiciwym kodzie obroc sie w tyl i porusz o jedno pole zmien wartosc course o +180
			self.setCourse(180)
		else:
			#we wlasiciwym kodzie obroc sie w lewo i porusz o jedno pole zmien wartosc course o +270
			self.setCourse(270)
			
		if self.course == 0: self.y = self.y + 1
		elif self.course == 90: self.x = self.x + 1
		elif self.course == 180: self.y = self.y - 1
		elif self.course == 270: self.x = self.x - 1
	
	
	
	
	
	