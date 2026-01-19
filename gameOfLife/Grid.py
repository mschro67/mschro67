#by mschro67

from random import randint

class Grid():
    def __init__(self,width,heigth):
        self.grid=[[randint(0,1) for x in range(width)] for y in range(heigth)]
        self.gen=0
    
    def setGrid(self,grid):
        self.grid=grid.copy()
    
    def display(self):
        string=""
        for row in self.grid:
            for col in row:
                if col==1:
                    string+="X"
                else:
                    string+="0"
                string+=" "
            string+="\n"
        print(string)
    
    def nextGen(self):
        self.gen+=1
        self.nextGrid=[[0 for x in range(len(self.grid[0]))] for y in range(len(self.grid))]
        self.alive=0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                neighbors=0
                for x in range(-1,2,1):
                    for y in range(-1,2,1):
                        try:
                            if self.grid[row+y][col+x]==1:
                                neighbors+=1
                        except:
                            pass
                if self.grid[row][col]==1:
                    if neighbors == 3 or neighbors == 4:
                        self.nextGrid[row][col]=1
                        self.alive+=1
                elif self.grid[row][col]==0 and neighbors==3:
                    self.nextGrid[row][col]=1
                    self.alive+=1
        self.grid=self.nextGrid.copy()
        if self.alive==0:
            return 0
        return 1