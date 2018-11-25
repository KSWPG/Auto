from Package import RobotClass
from Package import SimulationMapMatrixClass
from FindWayClass import FindWayClass

import time

import numpy as np

def mappingAlgorithm1(robot):
	while True:
		robot.checkSensor()
		try:
			#findWay = FindWayClass(robot.map)
			#pathMap = findWay.findWayToNearestNoVisitedSpot(robot.position)
			pathMap = robot.map.findWayToNearestNoVisitedSpot(robot.position)
			robot.goByPath(pathMap)
		except Exception as e:
			if(str(e) == "Not found anymore no visited spot"):
				break
			else:
				raise Exception(e)

	robot.map.completeMapAfterMapping()

def mappingAlgorithm2(robot):
	while True:
		robot.checkSensor()
		try:
			#findWay = FindWayClass(robot.map)
			#pathMap = findWay.findWayToNearestNoVisitedSpot(robot.position)
			pathMap = robot.map.findWayToNearestNoVisitedSpot2(robot.position)
			robot.goByPath(pathMap)
		except Exception as e:
			if(str(e) == "Not found anymore no visited spot"):
				break
			else:
				raise Exception(e)

	robot.map.completeMapAfterMapping()


def testAlgorithmsHowManyMovesIsNeeded():
	better1 = 0
	better2 = 0
	equal = 0

	theBestMappingAlgorithm1Time= 0
	theBestMappingAlgorithm2Time = 0

	mappingAlgorithm1WasFaster = 0
	mappingAlgorithm2WasFaster = 0
	timeWasEqual = 0

	for i in range(0,100):
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
			mappingAlgorithm1WasFaster = mappingAlgorithm1WasFaster + 1
		elif(timeDifferecne<0):
			mappingAlgorithm2WasFaster = mappingAlgorithm2WasFaster + 1
		else:
			timeWasEqual = timeWasEqual + 1

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
		print(i)

	print("mappingAlgorithm1 wykonal mniej ruchow %i razy" % better1)
	print("mappingAlgorithm2 wykonal mniej ruchow %i razy" % better2)
	print("algorytmy wykonaly tyle samo ruchow %i razy" % equal)

	print("W najlepszym wypadku mappingAlgorithm1 byl szybszy o %f" % theBestMappingAlgorithm1Time)
	print("W najlepszym wypadku mappingAlgorithm2 byl szybszy o %f" % (theBestMappingAlgorithm2Time*(-1)))

	print("mappingAlgorithm1 byl szybszy %i razy" % mappingAlgorithm1WasFaster)
	print("mappingAlgorithm2 byl szybszy %i razy" % mappingAlgorithm2WasFaster)
	print("Algorytmy byly tak samo szybkie %i razy" % timeWasEqual)

def mappingTest():
	simulationMap = SimulationMapMatrixClass(25,10)
	simulationMap.generateRandomMap()
	simulationMap.drawMap()

	robot = RobotClass()
	robot.simulationMap = simulationMap
	mappingAlgorithm2(robot)
	robot.map.drawMap()

mappingTest()
