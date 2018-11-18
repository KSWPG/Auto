from Package import RobotClass
from Package import SimulationMapMatrixClass

import time

import numpy as np

def mappingAlgorithm1(robot):
	while True:
		#print("Size X: %i Y: %i" % (robot.map.xSize, robot.map.ySize))
		#print("Size in bytes: %i" % robot.map.mapMatrix.nbytes)
		robot.checkSensor()
		try:
			PathMap = robot.map.findWayToNearestNoVisitedSpot(robot.position)
			robot.goByPath(PathMap)
		except Exception as e:
			if(str(e) == "Not found anymore no visited spot"):
				break

	robot.map.completeMapAfterMapping()
	#print("Zakonczono proces mapowania w %i ruchach" % robot.moves)
	#robot.map.drawMatrix()

def mappingAlgorithm2(robot):
	while True:
		robot.checkSensor()
		try:
			PathMap = robot.map.findWayToNearestNoVisitedSpot2(robot.position)
			robot.goByPath(PathMap)
		except Exception as e:
			if(str(e) == "Not found anymore no visited spot"):
				break

	robot.map.completeMapAfterMapping()
	#print("Zakonczono proces mapowania w %i ruchach" % robot.moves)
	#robot.map.drawMatrix()


def testAlgorithmsHowManyMovesIsNeeded():
	better1 = 0
	better2 = 0

	theBestMappingAlgorithm1Time= 0
	theBestMappingAlgorithm2Time = 0

	MappingAlgorithm1WasFaster = 0
	MappingAlgorithm2WasFaster = 0
	TimeWasEqual = 0

	equal = 0
	for z in range(0,100):
		simulationMap = SimulationMapMatrixClass(10,10)
		simulationMap.generateRandomMap()
		robot = RobotClass()
		robot.simulationMap=simulationMap

		start_time = time.time()
		mappingAlgorithm1(robot)
		mappingAlgorithm1Time = time.time()-start_time
		algorithm1Moves = robot.moves

		robot2 = RobotClass()
		robot2.simulationMap = simulationMap

		start_time = time.time()
		mappingAlgorithm2(robot2)
		mappingAlgorithm2Time = time.time()-start_time
		algorithm2Moves = robot2.moves

		timeDifferecne = mappingAlgorithm2Time - mappingAlgorithm1Time

		if(timeDifferecne>0):
			MappingAlgorithm1WasFaster = MappingAlgorithm1WasFaster +1
		elif(timeDifferecne<0):
			MappingAlgorithm2WasFaster = MappingAlgorithm2WasFaster +1
		else:
			TimeWasEqual = TimeWasEqual +1

		if (timeDifferecne > theBestMappingAlgorithm1Time):
			theBestMappingAlgorithm1Time = timeDifferecne
		elif(timeDifferecne < theBestMappingAlgorithm2Time):
			theBestMappingAlgorithm2Time = timeDifferecne

		if (algorithm1Moves < algorithm2Moves):
			 better1 = better1 + 1
		elif (algorithm1Moves > algorithm2Moves):
			better2 = better2 + 1
		else:
			equal = equal + 1
		print(z)

	print("mappingAlgorithm1 wykonal mniej ruchow %i razy" % better1)
	print("mappingAlgorithm2 wykonal mniej ruchow %i razy" % better2)
	print("algorytmy wykonaly tyle samo ruchow %i razy" % equal)

	print("W najlepszym wypadku mappingAlgorithm1 byl szybszy o %f" % theBestMappingAlgorithm1Time)
	print("W najlepszym wypadku mappingAlgorithm2 byl szybszy o %f" % (theBestMappingAlgorithm2Time*(-1)))

	print("mappingAlgorithm1 byl szybszy %i razy" % MappingAlgorithm1WasFaster)
	print("mappingAlgorithm2 byl szybszy %i razy" % MappingAlgorithm2WasFaster)
	print("Algorytmy byly tak samo szybkie %i razy" % TimeWasEqual)

def showHowManyMovesIsNeededToMap():
	matrix = np.zeros((100),dtype=np.byte)
	matrixNumber = 0
	for i in range(0,10):
		for j in range(0,10):
			robot = RobotClass()
			robot.position.x = i
			robot.position.y = j
			mappingAlgorithm1(robot)
			matrix[matrixNumber] = robot.moves

			matrix.sort()

	for i in range(0,100):
		print(matrix[i])

def quickTest():
	robot = RobotClass()
	mappingAlgorithm1(robot)
	robot.map.drawMap()

def mappingTest():
	simulationMap = SimulationMapMatrixClass(25,10)
	simulationMap.generateRandomMap()
	simulationMap.drawMap()
	robot = RobotClass()
	robot.simulationMap = simulationMap
	mappingAlgorithm1(robot)
	robot.map.drawMap()

mappingTest()
