from Package import mapMatrixClass

#Przygotowanie mapy która na czas pisania algorytmu będzie symulować odczyty z czujników
simulationMap = mapMatrixClass(10,10)		
simulationMap.prepareTable()
simulationMap.drawMatrix()