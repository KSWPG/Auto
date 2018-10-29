from Package import robotClass
import numpy as np

class mappingAlgorithm2:
	def __init__(self):
		print("Rozpoczecie procesu mapowania")
		self.robot = robotClass()
		#self.robot.checkSensor()
		#self.findNearestNoVisitedSpot()
		self.moves=0
		while True:
			self.robot.checkSensor()
			backPathMap = self.findNearestNoVisitedSpot()
			if(backPathMap[0][0] == -1): break
			
			self.goTo(backPathMap)
			
		print("Zakonczono proces mapowania w %i ruchach"%self.moves)
		self.robot.map.drawMatrix()
		
	def findNearestNoVisitedSpot(self):
		pathMap = np.zeros((10,10),dtype=np.byte)
		pathMap[self.robot.x][self.robot.y]=1
		actualValue=1
		findX=0
		findY=0
		endLoop=0
		#znajdz najblizszy nieodwiedzony punkt
		while (endLoop==0):
			changeAmount=0
			for i in range(0,10): 
				for j in range(0,10):
					if(pathMap[i][j] == actualValue):
						if(not self.robot.map.isWallExist(i,j,"W")):
							if(pathMap[i-1][j]==0):
								pathMap[i-1][j]=actualValue+1
								changeAmount=changeAmount+1
								if(not self.robot.map.wasVisited(i-1,j)): findX=i-1;findY=j;endLoop=1;break
						if(not self.robot.map.isWallExist(i,j,"N")):
							if(pathMap[i][j+1]==0):
								pathMap[i][j+1]=actualValue+1
								changeAmount=changeAmount+1
								if(not self.robot.map.wasVisited(i,j+1)): findX=i;findY=j+1;endLoop=1;break
						if(not self.robot.map.isWallExist(i,j,"E")):
							if(pathMap[i+1][j]==0):
								pathMap[i+1][j]=actualValue+1
								changeAmount=changeAmount+1
								if(not self.robot.map.wasVisited(i+1,j)): findX=i+1;findY=j;endLoop=1;break
						if(not self.robot.map.isWallExist(i,j,"S")):
							if(pathMap[i][j-1]==0):
								pathMap[i][j-1]=actualValue+1
								changeAmount=changeAmount+1
								if(not self.robot.map.wasVisited(i,j-1)): findX=i;findY=j-1;endLoop=1;break
					
						
					
					if(endLoop!=0):break
			actualValue = actualValue + 1
			if(changeAmount==0): 
				pathMap[0][0]=-1
				return pathMap  #zakonczono mapowanie 
		
		#print pathMap
		#wyznacz trase do znalecionego punktu
		backPathMap = np.zeros((10,10),dtype=np.byte)
		newValue = 1
		while (pathMap[findX][findY] != 1):
			backPathMap[findX][findY] = newValue
			if(findX != 9 and pathMap[findX+1][findY] == actualValue-1): findX = findX+1;actualValue = actualValue-1
			elif(findX !=0  and pathMap[findX-1][findY] == actualValue-1): findX = findX-1;actualValue = actualValue-1
			elif(findY != 9 and pathMap[findX][findY+1] == actualValue-1): findY = findY+1;actualValue = actualValue-1
			elif(findY != 0 and pathMap[findX][findY-1] == actualValue-1): findY = findY-1;actualValue = actualValue-1
			
			newValue = newValue+1

		backPathMap[findX][findY] = newValue
		#print backPathMap
		return backPathMap
		
	def goTo(self,backPathMap):
		while (backPathMap[self.robot.x][self.robot.y] != 1):
			actualValue = backPathMap[self.robot.x][self.robot.y]
			
			if self.robot.course == 0:
				if(self.robot.x != 9 and backPathMap[self.robot.x+1][self.robot.y] == actualValue-1):
					self.robot.go("R")
				elif(self.robot.x != 0 and backPathMap[self.robot.x-1][self.robot.y] == actualValue-1):
					self.robot.go("L")
				elif(self.robot.y != 9 and backPathMap[self.robot.x][self.robot.y+1] == actualValue-1):
					self.robot.go()
				elif(self.robot.y != 0 and backPathMap[self.robot.x][self.robot.y-1] == actualValue-1):
					self.robot.go("B")

						
			elif self.robot.course == 90:
				if(self.robot.x != 9 and backPathMap[self.robot.x+1][self.robot.y] == actualValue-1):
					self.robot.go()
				elif(self.robot.x != 0 and backPathMap[self.robot.x-1][self.robot.y] == actualValue-1):
					self.robot.go("B")
				elif(self.robot.y != 9 and backPathMap[self.robot.x][self.robot.y+1] == actualValue-1):
					self.robot.go("L")
				elif(self.robot.y != 0 and backPathMap[self.robot.x][self.robot.y-1] == actualValue-1):
					self.robot.go("R")
						
			elif self.robot.course == 180:
				if(self.robot.x != 9 and backPathMap[self.robot.x+1][self.robot.y] == actualValue-1):
					self.robot.go("L")
				elif(self.robot.x != 0 and backPathMap[self.robot.x-1][self.robot.y] == actualValue-1):
					self.robot.go("R")
				elif(self.robot.y != 9 and backPathMap[self.robot.x][self.robot.y+1] == actualValue-1):
					self.robot.go("B")
				elif(self.robot.y != 0 and backPathMap[self.robot.x][self.robot.y-1] == actualValue-1):
					self.robot.go()
						
			elif self.robot.course == 270:
				if(self.robot.x != 9 and backPathMap[self.robot.x+1][self.robot.y] == actualValue-1):
					self.robot.go("B")
				elif(self.robot.x != 0 and backPathMap[self.robot.x-1][self.robot.y] == actualValue-1):
					self.robot.go()
				elif(self.robot.y != 9 and backPathMap[self.robot.x][self.robot.y+1] == actualValue-1):
					self.robot.go("R")
				elif(self.robot.y != 0 and backPathMap[self.robot.x][self.robot.y-1] == actualValue-1):
					self.robot.go("L")
		
			self.moves=self.moves+1

		
mappingAlgorithm2()	