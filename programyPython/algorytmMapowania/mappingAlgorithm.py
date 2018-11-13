from Package import robotClass
from Package import simulationMapMatrixClass

import time

import numpy as np

def mappingAlgorithm1(robot):
	while True:
		print("X: %i Y: %i" % (robot.map.xSize, robot.map.ySize))
		robot.checkSensor()
		try:
			PathMap = robot.map.findWayToNearestNoVisitedSpot(robot.x,robot.y)
			robot.goByPath(PathMap)
		except Exception as e:
			if(str(e) == "Not found anymore no visited spot"):
				break



	#print("Zakonczono proces mapowania w %i ruchach" % robot.moves)
	#robot.map.drawMatrix()

def mappingAlgorithm2(robot):
	while True:
		robot.checkSensor()
		try:
			PathMap = robot.map.findWayToNearestNoVisitedSpot2(robot.x,robot.y,robot.course)
			robot.goByPath(PathMap)
		except Exception as e:
			if(str(e) == "Not found anymore no visited spot"):
				break

	#print("Zakonczono proces mapowania w %i ruchach" % robot.moves)
	#robot.map.drawMatrix()


def testAlgorithmsHowManyMovesIsNeeded():
	better1 = 0
	better2 = 0
	theBestMappingAlgorithm1Time= 0
	theBestMappingAlgorithm2Time = 0
	equal = 0
	for z in range(0,10):
		simulationMap = simulationMapMatrixClass(10,10)
		simulationMap.generateRandomMap()
		for i in range(0,simulationMap.xSize):
			for j in range(0,simulationMap.ySize):
				for k in [0,90,180,270]:
					robot = robotClass()
					robot.x = i
					robot.y = j
					robot.simulationMap=simulationMap

					start_time = time.time()
					mappingAlgorithm1(robot)
					mappingAlgorithm1Time = time.time()-start_time
					algorithm1Moves = robot.moves

					robot2 = robotClass()
					robot2.x = i
					robot2.y = j
					robot2.course = k
					robot2.simulationMap = simulationMap

					start_time = time.time()
					mappingAlgorithm2(robot2)
					mappingAlgorithm2Time = time.time()-start_time
					algorithm2Moves = robot2.moves

					timeDifferecne = mappingAlgorithm2Time - mappingAlgorithm1Time
					if (timeDifferecne > theBestMappingAlgorithm1Time):
						theBestMappingAlgorithm1Time = timeDifferecne
					elif(timeDifferecne < theBestMappingAlgorithm2Time):
						theBestMappingAlgorithm2Time = timeDifferecne

					if (algorithm1Moves < algorithm2Moves): better1 = better1 + 1
					elif (algorithm1Moves > algorithm2Moves): better2 = better2 + 1
					else: equal = equal + 1
		print(z)

	print("mappingAlgorithm1 byl lepszy %i razy" % better1)
	print("mappingAlgorithm2 byl lepszy %i razy" % better2)
	print("algorytmy byly sobie rowne %i razy" % equal)

	print("W najlepszym wypadku mappingAlgorithm1 byl szybszy o %f" % theBestMappingAlgorithm1Time)
	print("W najlepszym wypadku mappingAlgorithm2 byl szybszy o %f" % (theBestMappingAlgorithm2Time*(-1)))


def showHowManyMovesIsNeededToMap():
	matrix = np.zeros((100),dtype=np.byte)
	matrixNumber = 0
	for i in range(0,10):
		for j in range(0,10):
			robot = robotClass()
			robot.x = i
			robot.y = j
			mappingAlgorithm1(robot)
			matrix[matrixNumber] = robot.moves

			matrix.sort()

	for i in range(0,100):
		print(matrix[i])

def quickTest():
	robot = robotClass()
	mappingAlgorithm1(robot)
	robot.map.drawMap()

quickTest()
