from Package import robotClass
import numpy as np

def mappingAlgorithm2(robot):
	#print("Rozpoczecie procesu mapowania")
	while True:
		robot.checkSensor()
		backPathMap = robot.map.findWayToNearestNoVisitedSpot(robot.x,robot.y)
		if(backPathMap[0][0] == -1): break

		robot.goTo(backPathMap)

	#print("Zakonczono proces mapowania w %i ruchach" % robot.moves)
	#robot.map.drawMatrix()
	return robot.moves

def mappingAlgorithm3(robot):
	#print("Rozpoczecie procesu mapowania")
	while True:
		robot.checkSensor()
		backPathMap = robot.map.findWayToNearestNoVisitedSpot2(robot.x,robot.y,robot.course)
		if(backPathMap[0][0] == -1): break

		robot.goTo(backPathMap)

	#print("Zakonczono proces mapowania w %i ruchach" % robot.moves)
	#robot.map.drawMatrix()


def testAlgorithmsHowManyMovesIsNeeded():
	better2 = 0
	better3 = 0
	equal = 0
	for i in range(0,10):
		for j in range(0,10):
			for k in [0,90,180,270]:
				robot = robotClass()
				robot.x = i
				robot.y = j
				mappingAlgorithm2(robot)
				algorithm2Moves = robot.moves
				robot2 = robotClass()
				robot.x = i
				robot.y = j
				robot.course = k
				mappingAlgorithm3(robot)
				algorithm3Moves = robot.moves

				if (algorithm2Moves < algorithm3Moves): better2 = better2 + 1
				elif (algorithm2Moves > algorithm3Moves): better3 = better3 + 1
				else: equal = equal + 1

	print("mappingAlgorithm2 byl lepszy %i razy" % better2)
	print("mappingAlgorithm3 byl lepszy %i razy" % better3)
	print("algorytmy byly sobie rowne %i razy" % equal)

def showHowManyMovesIsNeededToMap():
	matrix = np.zeros((100),dtype=np.byte)
	matrixNumber = 0
	for i in range(0,10):
		for j in range(0,10):
			robot = robotClass()
			robot.x = i
			robot.y = j
			mappingAlgorithm2(robot)
			matrix[matrixNumber] = robot.moves

			matrix.sort()

	for i in range(0,100):
		print(matrix[i])


showHowManyMovesIsNeededToMap()
