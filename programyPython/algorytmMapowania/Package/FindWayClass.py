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
        self.pathMap.fill(0)
        self.pathMap[robotPosition.x][robotPosition.y] = 1
        self.actualValue = 1
        foundPosition = PositionClass()

        while(True):
            self.changeAmount = 0
            position = PositionClass()
            for position.x in range(0,self.currentMap.xSize):
                for position.y in range(0,self.currentMap.ySize):
                    if(self.pathMap[position.x][position.y] == self.actualValue):
                        foundPosition.copyFrom(self.checkPositions(position))
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
        self.pathMap.fill(0)
        self.pathMap[robotPosition.x][robotPosition.y] = 1
        self.actualValue = 1
        foundPosition = PositionClass()

        while(True):
            self.changeAmount = 0
            position = PositionClass()
            position.course = robotPosition.course
            for position.x in range(0,self.currentMap.xSize):
                for position.y in range(0,self.currentMap.ySize):
                    if(self.pathMap[position.x][position.y] == self.actualValue):
                        foundPosition.copyFrom(self.checkPositions(position))
                        if(foundPosition.x != -1):
                            return foundPosition
            self.actualValue = self.actualValue + 1
            if(self.changeAmount == 0):
                raise Exception("Not found anymore no visited spot")

    def checkPositions(self,position):
        positionToCheck = PositionClass()
        i = position.course
        for j in range(0,4):
            positionToCheck.copyFrom(self.preparePositionToCheck(i,position))
            directionToCheck = self.prepareDirectionToCheck(i)

            if(not self.currentMap.isWallExist(position,directionToCheck)):
                if(self.pathMap[positionToCheck.x][positionToCheck.y] == 0):
                    self.pathMap[positionToCheck.x][positionToCheck.y] = self.actualValue + 1
                    self.changeAmount = self.changeAmount + 1
                    if(not self.currentMap.wasVisited(positionToCheck)):
                        return positionToCheck
            i = i + 90

        positionToCheck.x = -1
        return positionToCheck

    def preparePositionToCheck(self,iteration,position):
        positionToCheck = PositionClass()
        positionToCheck.copyFrom(position)

        if((iteration/90) % 4 == 0):
            positionToCheck.x = positionToCheck.x - 1
        elif((iteration/90) % 4 == 1):
            positionToCheck.y = positionToCheck.y + 1
        elif((iteration/90) % 4 == 2):
            positionToCheck.x = positionToCheck.x + 1
        elif((iteration/90) % 4 == 3):
            positionToCheck.y = positionToCheck.y - 1

        return positionToCheck

    def prepareDirectionToCheck(self,iteration):
        directionToCheck = Direction.MAP_LEFT

        if((iteration/90) % 4 == 0):
            directionToCheck = Direction.MAP_LEFT
        elif((iteration/90) % 4 == 1):
            directionToCheck = Direction.MAP_TOP
        elif((iteration/90) % 4 == 2):
            directionToCheck = Direction.MAP_RIGHT
        elif((iteration/90) % 4 == 3):
            directionToCheck = Direction.MAP_BOTTOM

        return directionToCheck

    def findPathTo(self,fromPosition,toPosition):
        fromPosition.course = 0
        toPosition.course = 0

        self.pathMap.fill(0)
        self.pathMap[toPosition.x][toPosition.y] = 1
        print(self.pathMap)
        self.actualValue = 1
        while (True):
            self.changeAmount = 0
            position = PositionClass()
            for position.x in range(0,self.currentMap.xSize):
                for position.y in range(0,self.currentMap.ySize):
                    if(self.pathMap[position.x][position.y] == self.actualValue):
                        if (self.checkPositionsForFindPath(position,fromPosition,toPosition)):
                            return self.pathMap

            self.actualValue = self.actualValue + 1
            print("cos",self.changeAmount)
            if(self.changeAmount == 0):
                raise Exception("There is no way to the given point")

        #print pathMap
        return self.pathMap

    def checkPositionsForFindPath(self,position,fromPosition,toPosition):
        positionToCheck = PositionClass()
        i = position.course
        for j in range(0,4):
            positionToCheck.copyFrom(self.preparePositionToCheck(i,position))
            directionToCheck = self.prepareDirectionToCheck(i)

            if(self.checkRangeOfIndex(positionToCheck)):
                if(not self.currentMap.isWallExist(position,directionToCheck)):
                    if(self.pathMap[positionToCheck.x][positionToCheck.y] == 0):
                        print("cos")
                        self.pathMap[positionToCheck.x][positionToCheck.y] = self.actualValue + 1
                        self.changeAmount = self.changeAmount + 1
                        print(self.changeAmount)
                        if(fromPosition == toPosition):
                            return True
            i = i + 90

        return False

    def checkRangeOfIndex(self,position):
        if(position.x<0 or position.x >= self.currentMap.xSize):
            return False
        elif(position.y<0 or position.y >= self.currentMap.ySize):
            return False
        else:
            return True
