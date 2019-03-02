class PositionClass:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.course = 0

    def copyFrom(self,position):
        self.x = position.x
        self.y = position.y
        self.course = position.course

    def __eq__(self,other):
        if isinstance(other, PositionClass):
            return (self.x == other.x and self.y == other.y and self.course == other.course)
        return False

    def __ne__(self,other):
        return not self.__eq__(other)


    def addToCourse(self,angle):
        if(angle == 90 or angle == 180 or angle == 270):
            self.course = self.course + angle
            if(self.course < 360):
                pass
            elif(self.course == 360):
                self.course = 0
            elif(self.course == 450):
                self.course = 90
            elif(self.course == 540):
                self.course = 180
        else:
            raise Exception("The value of the angle should be 90,180 or 270.")

    def goOneFieldForward(self):
        if(self.course == 0):
            self.y = self.y + 1
        elif(self.course == 90):
            self.x = self.x + 1
        elif(self.course == 180):
            self.y = self.y - 1
        elif(self.course == 270):
            self.x = self.x - 1
