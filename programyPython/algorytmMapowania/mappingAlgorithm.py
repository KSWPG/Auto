from Package import robotClass

class mappingAlgorithm:
	def __init__(self):
		print("Rozpoczecie procesu mapowania")
		self.robot = robotClass()
		if(self.checkEdge()):
			print("Zmapowano krawedz obszaru")
			self.robot.map.drawMatrix()
			#dalsza czesc programu

	def checkEdge(self):
		while True:
			self.robot.checkSensor()
			if self.robot.course == 0:
				if(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"W")):
					self.robot.go("L")
				elif(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"N")):
					self.robot.go()
				elif(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"E")):
					self.robot.go("R")
				elif(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"S")):
					self.robot.go("B")
				else:
					print("Robot nie moze wykonac ruchu")
					return False
					
			elif self.robot.course == 90:
				if(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"N")):
					self.robot.go("L")
				elif(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"E")):
					self.robot.go()
				elif(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"S")):
					self.robot.go("R")
				elif(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"W")):
					self.robot.go("B")
				else:
					print("Robot nie moze wykonac ruchu")
					return False
					
			elif self.robot.course == 180:
				if(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"E")):
					self.robot.go("L")
				elif(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"S")):
					self.robot.go()
				elif(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"W")):
					self.robot.go("R")
				elif(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"N")):
					self.robot.go("B")
				else:
					print("Robot nie moze wykonac ruchu")
					return False
					
			elif self.robot.course == 270:
				if(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"S")):
					self.robot.go("L")
				elif(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"W")):
					self.robot.go()
				elif(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"N")):
					self.robot.go("R")
				elif(not self.robot.map.isWallExist(self.robot.x,self.robot.y,"E")):
					self.robot.go("B")
				else:
					print("Robot nie moze wykonac ruchu")
					return False
			if(self.robot.x == self.robot.startX and self.robot.y == self.robot.startY): 
				return True
		

mappingAlgorithm()