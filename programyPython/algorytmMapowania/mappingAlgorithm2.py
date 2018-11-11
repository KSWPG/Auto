from Package import robotClass
from Package import mapMatrixClass
import time

import numpy as np

def mappingAlgorithm2(robot):
	while True:
		robot.checkSensor()
		try:
			PathMap = robot.map.findWayToNearestNoVisitedSpot(robot.x,robot.y)
			robot.goTo(PathMap)
		except Exception as e:
			if(str(e) == "Not found anymore no visited spot"):
				break



	#print("Zakonczono proces mapowania w %i ruchach" % robot.moves)
	#robot.map.drawMatrix()

def mappingAlgorithm3(robot):
	while True:
		robot.checkSensor()
		try:
			PathMap = robot.map.findWayToNearestNoVisitedSpot2(robot.x,robot.y,robot.course)
			robot.goTo(PathMap)
		except Exception as e:
			if(str(e) == "Not found anymore no visited spot"):
				break

	#print("Zakonczono proces mapowania w %i ruchach" % robot.moves)
	#robot.map.drawMatrix()


def testAlgorithmsHowManyMovesIsNeeded():
	better2 = 0
	better3 = 0
	theBestMappingAlgorithm2Time= 0
	theBestMappingAlgorithm3Time = 0
	equal = 0
	for z in range(0,10):
		simulationMap = mapMatrixClass(100,100)
		simulationMap.generateRandomMap()
		for i in range(0,simulationMap.xSize):
			for j in range(0,simulationMap.ySize):
				for k in [0,90,180,270]:
					robot = robotClass()
					robot.x = i
					robot.y = j
					robot.simulationMap=simulationMap

					start_time = time.time()
					mappingAlgorithm2(robot)
					mappingAlgorithm2Time = time.time()-start_time
					algorithm2Moves = robot.moves

					robot2 = robotClass()
					robot2.x = i
					robot2.y = j
					robot2.course = k
					robot2.simulationMap = simulationMap

					start_time = time.time()
					mappingAlgorithm3(robot2)
					mappingAlgorithm3Time = time.time()-start_time
					algorithm3Moves = robot2.moves

					timeDifferecne = mappingAlgorithm3Time - mappingAlgorithm2Time
					if (timeDifferecne > theBestMappingAlgorithm2Time):
						theBestMappingAlgorithm2Time = timeDifferecne
					elif(timeDifferecne < theBestMappingAlgorithm3Time):
						theBestMappingAlgorithm3Time = timeDifferecne

					if (algorithm2Moves < algorithm3Moves): better2 = better2 + 1
					elif (algorithm2Moves > algorithm3Moves): better3 = better3 + 1
					else: equal = equal + 1
		print(z)

	print("mappingAlgorithm2 byl lepszy %i razy" % better2)
	print("mappingAlgorithm3 byl lepszy %i razy" % better3)
	print("algorytmy byly sobie rowne %i razy" % equal)

	print("W najlepszym wypadku mappingAlgorithm2 byl szybszy o %f" % theBestMappingAlgorithm2Time)
	print("W najlepszym wypadku mappingAlgorithm3 byl szybszy o %f" % (theBestMappingAlgorithm3Time*(-1)))


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


testAlgorithmsHowManyMovesIsNeeded()
