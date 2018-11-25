import numpy as np

from MapMatrixClass import *
from DirectionEnum import DirectionEnum as Direction
from PositionClass import PositionClass

class FindWayClass:
    def __init__(self,currentMap):
        self.currentMap = currentMap
        self.actualValue = 1
        self.changeAmount = 0
        self.pathMap = np.zeros((self.currentMap.xSize,self.currentMap.ySize),dtype=np.byte)

    def findWayToNearestNoVisitedSpot(self,robotPosition):
        foundNoVisitedSpot = PositionClass()
        foundNoVisitedSpot.copyFrom(self.findNearestNoVisitedSpot(robotPosition))
        return self.findPathTo(robotPosition,foundNoVisitedSpot)

    def findNearestNoVisitedSpot(self,robotPosition):
        self.pathMap[robotPosition.x][robotPosition.y] = 1
        foundPosition = PositionClass()

        while(True):
            self.changeAmount = 0
            position = PositionClass()
            for position.x in range(0,self.currentMap.xSize):
                for position.y in range(0,self.currentMap.ySize):
                    if(self.pathMap[position.x][position.y] == self.actualValue):
                        foundPosition.copyFrom(self.checkPosition(position))
                        if(foundPosition.x != -1):
                            return foundPosition
            self.actualValue = self.actualValue + 1
            if(self.changeAmount == 0):
                raise Exception("Not found anymore no visited spot")

    def findWayToNearestNoVisitedSpot2(self,robotPosition):
        foundNoVisitedSpot = PositionClass()
        foundNoVisitedSpot.copyFrom(self.findNearestNoVisitedSpot2(robotPosition))
        return self.findPathTo(robotPosition,foundNoVisitedSpot)

    def findNearestNoVisitedSpot2(self,robotPosition):
        self.pathMap[robotPosition.x][robotPosition.y] = 1
        foundPosition = PositionClass()

        while(True):
            self.changeAmount = 0
            position = PositionClass()
            position.copyFrom(robotPosition)
            for position.x in range(0,self.currentMap.xSize):
                for position.y in range(0,self.currentMap.ySize):
                    if(self.pathMap[position.x][position.y] == self.actualValue):
                        foundPosition.copyFrom(self.checkPosition(position))
                        if(foundPosition.x != -1):
                            return foundPosition
            self.actualValue = self.actualValue + 1
            if(self.changeAmount == 0):
                raise Exception("Not found anymore no visited spot")

    def checkPosition(self,position):
        positionToCheck = PositionClass()
        positionToCheck.course = position.course
        i = position.course
        for j in range(0,4):
            positionToCheck.copyFrom(position)

            if((i/90) % 4 == 0):
                directionToCheck = Direction.MAP_LEFT
                positionToCheck.x = positionToCheck.x - 1
            elif((i/90) % 4 == 1):
                directionToCheck = Direction.MAP_TOP
                positionToCheck.y = positionToCheck.y + 1
            elif((i/90) % 4 == 2):
                directionToCheck = Direction.MAP_RIGHT
                positionToCheck.x = positionToCheck.x + 1
            elif((i/90) % 4 == 3):
                directionToCheck = Direction.MAP_BOTTOM
                positionToCheck.y = positionToCheck.y - 1

            if(not self.currentMap.isWallExist(position,directionToCheck)):
                if(self.pathMap[positionToCheck.x][positionToCheck.y] == 0):
                    self.pathMap[positionToCheck.x][positionToCheck.y] = self.actualValue + 1
                    self.changeAmount = self.changeAmount + 1
                    if(not self.currentMap.wasVisited(positionToCheck)):
                        return positionToCheck
            i = i + 90

        positionToCheck.x = -1
        return positionToCheck

    def findPathTo(self,fromPosition,toPosition):
        fromPosition.course = 0
        toPosition.course = 0

        pathMap = np.zeros((self.currentMap.xSize,self.currentMap.ySize),dtype=np.byte)
        pathMap[toPosition.x][toPosition.y] = 1

        actualValue = 1
        endLoop=0
        while (endLoop==0):
            position = PositionClass()
            for position.x in range(0,self.currentMap.xSize):
                for position.y in range(0,self.currentMap.ySize):
                    if(pathMap[position.x][position.y] == actualValue):
                        if(position.x != 0 and not self.currentMap.isWallExist(position,Direction.MAP_LEFT)):
                            positionToCheck = PositionClass()
                            positionToCheck.copyFrom(position)
                            positionToCheck.x = positionToCheck.x - 1
                            if(pathMap[positionToCheck.x][positionToCheck.y]==0):
                                pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
                                if(positionToCheck.x == fromPosition.x and positionToCheck.y == fromPosition.y):
                                    endLoop = 1
                                    break
                        if(position.y != self.currentMap.ySize-1 and not self.currentMap.isWallExist(position,Direction.MAP_TOP)):
                            positionToCheck = PositionClass()
                            positionToCheck.copyFrom(position)
                            positionToCheck.y = positionToCheck.y + 1
                            if(pathMap[positionToCheck.x][positionToCheck.y]==0):
                                pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
                                if(positionToCheck.x == fromPosition.x and positionToCheck.y == fromPosition.y):
                                    endLoop = 1
                                    break
                        if(position.x != self.currentMap.xSize-1 and not self.currentMap.isWallExist(position,Direction.MAP_RIGHT)):
                            positionToCheck = PositionClass()
                            positionToCheck.copyFrom(position)
                            positionToCheck.x = positionToCheck.x + 1
                            if(pathMap[positionToCheck.x][positionToCheck.y]==0):
                                pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
                                if(positionToCheck.x == fromPosition.x and positionToCheck.y == fromPosition.y):
                                    endLoop = 1
                                    break
                        if(position.y !=0 and not self.currentMap.isWallExist(position,Direction.MAP_BOTTOM)):
                            positionToCheck = PositionClass()
                            positionToCheck.copyFrom(position)
                            positionToCheck.y = positionToCheck.y - 1
                            if(pathMap[positionToCheck.x][positionToCheck.y]==0):
                                pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
                                if(positionToCheck == fromPosition ):
                                    endLoop = 1
                                    break
                if(endLoop!=0):
                    break
            actualValue = actualValue + 1

        #print pathMap
        return pathMap
