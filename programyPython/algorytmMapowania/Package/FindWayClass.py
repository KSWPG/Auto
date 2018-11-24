import numpy as np

from DirectionEnum import DirectionEnum as Direction
from PositionClass import PositionClass
#from MapMatrixClass import MapMatrixClass

def __init__(self,currentMap):
    self.currentMap = currentMap
    self.actualValue = 1
    self.changeAmount = 0
    self.pathMap = np.zeros((self.xSize,self.ySize),dtype=np.byte)

def findWayToNearestNoVisitedSpot(self,robotPosition):
    foundNoVisitedSpot = PositionClass()
    foundNoVisitedSpot.copyFrom(self.findNearestNoVisitedSpot(robotPosition))
    return findPathTo

def findNearestNoVisitedSpot(self,robotPosition):
    self.pathMap[robotPosition.x][robotPosition.y] = 1
    foundPosition = PositionClass()

    while (True):
        changeAmount = 0
        position = PositionClass()
        for position.x in range(0,self.xSize):
            for position.y in range(0,self.ySize):
                if(pathMap[position.x][position.y] == actualValue):
                    foundPosition.copyFrom(self.checkPosition(position))
                    if(foundPosition.x != -1):
                        return foundPosition
        actualValue = actualValue + 1
        if(changeAmount==0):
            raise Exception("Not found anymore no visited spot")

def checkPosition(self,position):
    positionToCheck = PositionClass()
    positionToCheck.course = position.course
    for i in range(0,4):
        positionToCheck.copyFrom(position)
        if((positionToCheck.course/90) % 4 == 0):
            directionToCheck = Direction.MAP_LEFT
            positionToCheck.x = positionToCheck.x - 1
        elif((positionToCheck.course/90) % 4 == 0):
            directionToCheck = Direction.MAP_TOP
            positionToCheck.y = positionToCheck.y + 1
        elif((positionToCheck.course/90) % 4 == 0):
            directionToCheck = Direction.MAP_RIGHT
            positionToCheck.x = positionToCheck.x + 1
        elif((positionToCheck.course/90) % 4 == 0):
            directionToCheck = Direction.MAP_BOTTOM
            positionToCheck.y = positionToCheck.y - 1

        if(not self.currentMap.isWallExist(position,directionToCheck)):
            if(self.pathMap[positionToCheck.x][positionToCheck.y] == 0):
                self.pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
                changeAmount = changeAmount + 1
                if(not self.wasVisited(positionToCheck)):
                    return positionToCheck

        positionToCheck.x = -1
        return positionToCheck

def findPathTo(self,fromPosition,toPosition):
    fromPosition.course = 0
    toPosition.course = 0

    pathMap = np.zeros((self.xSize,self.ySize),dtype=np.byte)
    pathMap[toPosition.x][toPosition.y] = 1

    actualValue = 1
    endLoop=0
    while (endLoop==0):
        position = PositionClass()
        for position.x in range(0,self.xSize):
            for position.y in range(0,self.ySize):
                if(pathMap[position.x][position.y] == actualValue):
                    if(position.x != 0 and not self.isWallExist(position,Direction.MAP_LEFT)):
                        positionToCheck = PositionClass()
                        positionToCheck.copyFrom(position)
                        positionToCheck.x = positionToCheck.x - 1
                        if(pathMap[positionToCheck.x][positionToCheck.y]==0):
                            pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
                            if(positionToCheck.x == fromPosition.x and positionToCheck.y == fromPosition.y):
                                endLoop = 1
                                break
                    if(position.y != self.ySize-1 and not self.isWallExist(position,Direction.MAP_TOP)):
                        positionToCheck = PositionClass()
                        positionToCheck.copyFrom(position)
                        positionToCheck.y = positionToCheck.y + 1
                        if(pathMap[positionToCheck.x][positionToCheck.y]==0):
                            pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
                            if(positionToCheck.x == fromPosition.x and positionToCheck.y == fromPosition.y):
                                endLoop = 1
                                break
                    if(position.x != self.xSize-1 and not self.isWallExist(position,Direction.MAP_RIGHT)):
                        positionToCheck = PositionClass()
                        positionToCheck.copyFrom(position)
                        positionToCheck.x = positionToCheck.x + 1
                        if(pathMap[positionToCheck.x][positionToCheck.y]==0):
                            pathMap[positionToCheck.x][positionToCheck.y] = actualValue + 1
                            if(positionToCheck.x == fromPosition.x and positionToCheck.y == fromPosition.y):
                                endLoop = 1
                                break
                    if(position.y !=0 and not self.isWallExist(position,Direction.MAP_BOTTOM)):
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
