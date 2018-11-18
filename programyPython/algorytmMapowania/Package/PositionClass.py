class PositionClass:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.course = 0

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
