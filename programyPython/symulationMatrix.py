import numpy as np

symulationMatrix = np.arange(400).reshape(10,10,4).astype(np.byte)

#wiersz 0
symulationMatrix[0][0][0]=0
symulationMatrix[0][0][1]=4
symulationMatrix[0][0][2]=2
symulationMatrix[0][0][3]=0

symulationMatrix[0][1][0]=0
symulationMatrix[0][1][1]=3
symulationMatrix[0][1][2]=2
symulationMatrix[0][1][3]=1

symulationMatrix[0][2][0]=0
symulationMatrix[0][2][1]=2
symulationMatrix[0][2][2]=0
symulationMatrix[0][2][3]=2

symulationMatrix[0][3][0]=0
symulationMatrix[0][3][1]=1
symulationMatrix[0][3][2]=0
symulationMatrix[0][3][3]=3

symulationMatrix[0][4][0]=0
symulationMatrix[0][4][1]=0
symulationMatrix[0][4][2]=1
symulationMatrix[0][4][3]=4

symulationMatrix[0][5][0]=0
symulationMatrix[0][5][1]=4
symulationMatrix[0][5][2]=2
symulationMatrix[0][5][3]=0

symulationMatrix[0][6][0]=0
symulationMatrix[0][6][1]=3
symulationMatrix[0][6][2]=9
symulationMatrix[0][6][3]=1

symulationMatrix[0][7][0]=0
symulationMatrix[0][7][1]=2
symulationMatrix[0][7][2]=5
symulationMatrix[0][7][3]=2

symulationMatrix[0][8][0]=0
symulationMatrix[0][8][1]=1
symulationMatrix[0][8][2]=1
symulationMatrix[0][8][3]=3

symulationMatrix[0][9][0]=0
symulationMatrix[0][9][1]=0
symulationMatrix[0][9][2]=1
symulationMatrix[0][9][3]=4

#wiersz 1
symulationMatrix[1][0][0]=1
symulationMatrix[1][0][1]=1
symulationMatrix[1][0][2]=1
symulationMatrix[1][0][3]=0

symulationMatrix[1][1][0]=1
symulationMatrix[1][1][1]=0
symulationMatrix[1][1][2]=1
symulationMatrix[1][1][3]=1

symulationMatrix[1][2][0]=0
symulationMatrix[1][2][1]=1
symulationMatrix[1][2][2]=8
symulationMatrix[1][2][3]=0

symulationMatrix[1][3][0]=0
symulationMatrix[1][3][1]=0
symulationMatrix[1][3][2]=1
symulationMatrix[1][3][3]=1

symulationMatrix[1][4][0]=1
symulationMatrix[1][4][1]=0
symulationMatrix[1][4][2]=0
symulationMatrix[1][4][3]=0

symulationMatrix[1][5][0]=1
symulationMatrix[1][5][1]=4
symulationMatrix[1][5][2]=1
symulationMatrix[1][5][3]=0

symulationMatrix[1][6][0]=1
symulationMatrix[1][6][1]=3
symulationMatrix[1][6][2]=8
symulationMatrix[1][6][3]=1

symulationMatrix[1][7][0]=1
symulationMatrix[1][7][1]=2
symulationMatrix[1][7][2]=4
symulationMatrix[1][7][3]=2

symulationMatrix[1][8][0]=1
symulationMatrix[1][8][1]=1
symulationMatrix[1][8][2]=0
symulationMatrix[1][8][3]=3

symulationMatrix[1][9][0]=1
symulationMatrix[1][9][1]=0
symulationMatrix[1][9][2]=0
symulationMatrix[1][9][3]=4

#wiersz 2
symulationMatrix[2][0][0]=2
symulationMatrix[2][0][1]=1
symulationMatrix[2][0][2]=0
symulationMatrix[2][0][3]=0

symulationMatrix[2][1][0]=2
symulationMatrix[2][1][1]=0
symulationMatrix[2][1][2]=0
symulationMatrix[2][1][3]=1

symulationMatrix[2][2][0]=1
symulationMatrix[2][2][1]=5
symulationMatrix[2][2][2]=7
symulationMatrix[2][2][3]=0

symulationMatrix[2][3][0]=1
symulationMatrix[2][3][1]=4
symulationMatrix[2][3][2]=0
symulationMatrix[2][3][3]=1

symulationMatrix[2][4][0]=0
symulationMatrix[2][4][1]=3
symulationMatrix[2][4][2]=2
symulationMatrix[2][4][3]=2

symulationMatrix[2][5][0]=2
symulationMatrix[2][5][1]=2
symulationMatrix[2][5][2]=0
symulationMatrix[2][5][3]=3

symulationMatrix[2][6][0]=2
symulationMatrix[2][6][1]=1
symulationMatrix[2][6][2]=7
symulationMatrix[2][6][3]=4

symulationMatrix[2][7][0]=2
symulationMatrix[2][7][1]=0
symulationMatrix[2][7][2]=3
symulationMatrix[2][7][3]=5

symulationMatrix[2][8][0]=0
symulationMatrix[2][8][1]=1
symulationMatrix[2][8][2]=0
symulationMatrix[2][8][3]=0

symulationMatrix[2][9][0]=0
symulationMatrix[2][9][1]=0
symulationMatrix[2][9][2]=1
symulationMatrix[2][9][3]=1


#wiersz 3
symulationMatrix[3][0][0]=0
symulationMatrix[3][0][1]=2
symulationMatrix[3][0][2]=6
symulationMatrix[3][0][3]=0

symulationMatrix[3][1][0]=0
symulationMatrix[3][1][1]=1
symulationMatrix[3][1][2]=6
symulationMatrix[3][1][3]=1

symulationMatrix[3][2][0]=2
symulationMatrix[3][2][1]=0
symulationMatrix[3][2][2]=6
symulationMatrix[3][2][3]=2

symulationMatrix[3][3][0]=0
symulationMatrix[3][3][1]=0
symulationMatrix[3][3][2]=1
symulationMatrix[3][3][3]=0

symulationMatrix[3][4][0]=1
symulationMatrix[3][4][1]=0
symulationMatrix[3][4][2]=1
symulationMatrix[3][4][3]=0

symulationMatrix[3][5][0]=0
symulationMatrix[3][5][1]=0
symulationMatrix[3][5][2]=0
symulationMatrix[3][5][3]=0

symulationMatrix[3][6][0]=3
symulationMatrix[3][6][1]=2
symulationMatrix[3][6][2]=6
symulationMatrix[3][6][3]=0

symulationMatrix[3][7][0]=3
symulationMatrix[3][7][1]=1
symulationMatrix[3][7][2]=2
symulationMatrix[3][7][3]=1

symulationMatrix[3][8][0]=0
symulationMatrix[3][8][1]=0
symulationMatrix[3][8][2]=4
symulationMatrix[3][8][3]=2

symulationMatrix[3][9][0]=1
symulationMatrix[3][9][1]=0
symulationMatrix[3][9][2]=0
symulationMatrix[3][9][3]=0


#wiersz 4
symulationMatrix[4][0][0]=1
symulationMatrix[4][0][1]=2
symulationMatrix[4][0][2]=5
symulationMatrix[4][0][3]=0

symulationMatrix[4][1][0]=1
symulationMatrix[4][1][1]=1
symulationMatrix[4][1][2]=5
symulationMatrix[4][1][3]=1

symulationMatrix[4][2][0]=3
symulationMatrix[4][2][1]=0
symulationMatrix[4][2][2]=5
symulationMatrix[4][2][3]=2

symulationMatrix[4][3][0]=1
symulationMatrix[4][3][1]=2
symulationMatrix[4][3][2]=0
symulationMatrix[4][3][3]=0

symulationMatrix[4][4][0]=2
symulationMatrix[4][4][1]=1
symulationMatrix[4][4][2]=0
symulationMatrix[4][4][3]=1

symulationMatrix[4][5][0]=0
symulationMatrix[4][5][1]=0
symulationMatrix[4][5][2]=0
symulationMatrix[4][5][3]=2

symulationMatrix[4][6][0]=4
symulationMatrix[4][6][1]=3
symulationMatrix[4][6][2]=5
symulationMatrix[4][6][3]=0

symulationMatrix[4][7][0]=4
symulationMatrix[4][7][1]=2
symulationMatrix[4][7][2]=1
symulationMatrix[4][7][3]=1

symulationMatrix[4][8][0]=1
symulationMatrix[4][8][1]=1
symulationMatrix[4][8][2]=3
symulationMatrix[4][8][3]=2

symulationMatrix[4][9][0]=0
symulationMatrix[4][9][1]=0
symulationMatrix[4][9][2]=5
symulationMatrix[4][9][3]=3


#wiersz 5
symulationMatrix[5][0][0]=2
symulationMatrix[5][0][1]=8
symulationMatrix[5][0][2]=4
symulationMatrix[5][0][3]=0

symulationMatrix[5][1][0]=2
symulationMatrix[5][1][1]=7
symulationMatrix[5][1][2]=4
symulationMatrix[5][1][3]=1

symulationMatrix[5][2][0]=4
symulationMatrix[5][2][1]=6
symulationMatrix[5][2][2]=4
symulationMatrix[5][2][3]=2

symulationMatrix[5][3][0]=0
symulationMatrix[5][3][1]=5
symulationMatrix[5][3][2]=4
symulationMatrix[5][3][3]=3

symulationMatrix[5][4][0]=0
symulationMatrix[5][4][1]=4
symulationMatrix[5][4][2]=1
symulationMatrix[5][4][3]=4

symulationMatrix[5][5][0]=0
symulationMatrix[5][5][1]=3
symulationMatrix[5][5][2]=1
symulationMatrix[5][5][3]=5

symulationMatrix[5][6][0]=5
symulationMatrix[5][6][1]=2
symulationMatrix[5][6][2]=4
symulationMatrix[5][6][3]=6

symulationMatrix[5][7][0]=5
symulationMatrix[5][7][1]=1
symulationMatrix[5][7][2]=0
symulationMatrix[5][7][3]=7

symulationMatrix[5][8][0]=2
symulationMatrix[5][8][1]=0
symulationMatrix[5][8][2]=2
symulationMatrix[5][8][3]=8

symulationMatrix[5][9][0]=1
symulationMatrix[5][9][1]=0
symulationMatrix[5][9][2]=4
symulationMatrix[5][9][3]=0


#wiersz 6
symulationMatrix[6][0][0]=3
symulationMatrix[6][0][1]=7
symulationMatrix[6][0][2]=3
symulationMatrix[6][0][3]=0

symulationMatrix[6][1][0]=3
symulationMatrix[6][1][1]=6
symulationMatrix[6][1][2]=3
symulationMatrix[6][1][3]=1

symulationMatrix[6][2][0]=5
symulationMatrix[6][2][1]=5
symulationMatrix[6][2][2]=3
symulationMatrix[6][2][3]=2

symulationMatrix[6][3][0]=1
symulationMatrix[6][3][1]=4
symulationMatrix[6][3][2]=3
symulationMatrix[6][3][3]=3

symulationMatrix[6][4][0]=1
symulationMatrix[6][4][1]=3
symulationMatrix[6][4][2]=0
symulationMatrix[6][4][3]=4

symulationMatrix[6][5][0]=1
symulationMatrix[6][5][1]=2
symulationMatrix[6][5][2]=0
symulationMatrix[6][5][3]=5

symulationMatrix[6][6][0]=6
symulationMatrix[6][6][1]=1
symulationMatrix[6][6][2]=3
symulationMatrix[6][6][3]=6

symulationMatrix[6][7][0]=0
symulationMatrix[6][7][1]=0
symulationMatrix[6][7][2]=0
symulationMatrix[6][7][3]=7

symulationMatrix[6][8][0]=3
symulationMatrix[6][8][1]=0
symulationMatrix[6][8][2]=1
symulationMatrix[6][8][3]=0

symulationMatrix[6][9][0]=2
symulationMatrix[6][9][1]=0
symulationMatrix[6][9][2]=3
symulationMatrix[6][9][3]=0


#wiersz 7
symulationMatrix[7][0][0]=4
symulationMatrix[7][0][1]=3
symulationMatrix[7][0][2]=2
symulationMatrix[7][0][3]=0

symulationMatrix[7][1][0]=4
symulationMatrix[7][1][1]=2
symulationMatrix[7][1][2]=2
symulationMatrix[7][1][3]=1

symulationMatrix[7][2][0]=6
symulationMatrix[7][2][1]=1
symulationMatrix[7][2][2]=2
symulationMatrix[7][2][3]=2

symulationMatrix[7][3][0]=2
symulationMatrix[7][3][1]=0
symulationMatrix[7][3][2]=2
symulationMatrix[7][3][3]=3

symulationMatrix[7][4][0]=0
symulationMatrix[7][4][1]=1
symulationMatrix[7][4][2]=2
symulationMatrix[7][4][3]=0

symulationMatrix[7][5][0]=0
symulationMatrix[7][5][1]=0
symulationMatrix[7][5][2]=1
symulationMatrix[7][5][3]=1

symulationMatrix[7][6][0]=7
symulationMatrix[7][6][1]=0
symulationMatrix[7][6][2]=2
symulationMatrix[7][6][3]=0

symulationMatrix[7][7][0]=0
symulationMatrix[7][7][1]=1
symulationMatrix[7][7][2]=2
symulationMatrix[7][7][3]=0

symulationMatrix[7][8][0]=4
symulationMatrix[7][8][1]=0
symulationMatrix[7][8][2]=0
symulationMatrix[7][8][3]=1

symulationMatrix[7][9][0]=3
symulationMatrix[7][9][1]=0
symulationMatrix[7][9][2]=2
symulationMatrix[7][9][3]=0


#wiersz 8
symulationMatrix[8][0][0]=5
symulationMatrix[8][0][1]=4
symulationMatrix[8][0][2]=1
symulationMatrix[8][0][3]=0

symulationMatrix[8][1][0]=5
symulationMatrix[8][1][1]=3
symulationMatrix[8][1][2]=1
symulationMatrix[8][1][3]=1

symulationMatrix[8][2][0]=7
symulationMatrix[8][2][1]=2
symulationMatrix[8][2][2]=1
symulationMatrix[8][2][3]=2

symulationMatrix[8][3][0]=3
symulationMatrix[8][3][1]=1
symulationMatrix[8][3][2]=1
symulationMatrix[8][3][3]=3

symulationMatrix[8][4][0]=1
symulationMatrix[8][4][1]=0
symulationMatrix[8][4][2]=1
symulationMatrix[8][4][3]=4

symulationMatrix[8][5][0]=1
symulationMatrix[8][5][1]=0
symulationMatrix[8][5][2]=0
symulationMatrix[8][5][3]=0

symulationMatrix[8][6][0]=8
symulationMatrix[8][6][1]=0
symulationMatrix[8][6][2]=1
symulationMatrix[8][6][3]=0

symulationMatrix[8][7][0]=1
symulationMatrix[8][7][1]=0
symulationMatrix[8][7][2]=1
symulationMatrix[8][7][3]=0

symulationMatrix[8][8][0]=0
symulationMatrix[8][8][1]=1
symulationMatrix[8][8][2]=1
symulationMatrix[8][8][3]=0

symulationMatrix[8][9][0]=4
symulationMatrix[8][9][1]=0
symulationMatrix[8][9][2]=1
symulationMatrix[8][9][3]=1


symulationMatrix[9][0][0]=6
symulationMatrix[9][0][1]=7
symulationMatrix[9][0][2]=0
symulationMatrix[9][0][3]=0

symulationMatrix[9][1][0]=6
symulationMatrix[9][1][1]=6
symulationMatrix[9][1][2]=0
symulationMatrix[9][1][3]=1

symulationMatrix[9][2][0]=8
symulationMatrix[9][2][1]=5
symulationMatrix[9][2][2]=0
symulationMatrix[9][2][3]=2

symulationMatrix[9][3][0]=4
symulationMatrix[9][3][1]=4
symulationMatrix[9][3][2]=0
symulationMatrix[9][3][3]=3

symulationMatrix[9][4][0]=2
symulationMatrix[9][4][1]=3
symulationMatrix[9][4][2]=0
symulationMatrix[9][4][3]=4

symulationMatrix[9][5][0]=0
symulationMatrix[9][5][1]=2
symulationMatrix[9][5][2]=0
symulationMatrix[9][5][3]=5

symulationMatrix[9][6][0]=9
symulationMatrix[9][6][1]=1
symulationMatrix[9][6][2]=0
symulationMatrix[9][6][3]=6

symulationMatrix[9][7][0]=2
symulationMatrix[9][7][1]=0
symulationMatrix[9][7][2]=0
symulationMatrix[9][7][3]=7

symulationMatrix[9][8][0]=1
symulationMatrix[9][8][1]=1
symulationMatrix[9][8][2]=0
symulationMatrix[9][8][3]=0

symulationMatrix[9][9][0]=5
symulationMatrix[9][9][1]=0
symulationMatrix[9][9][2]=0
symulationMatrix[9][9][3]=1