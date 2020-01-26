import random
import numpy as np
class life ():
    def __init__(self):
        self.grid = np.array([[random.randint(0,1)]*8 for _ in range(8)])
        self.temp = np.copy(self.grid)
        self.r = len(self.grid)
        self.c = len(self.grid[0])
        self.generation =  0
        
        
    
    
    def check(self):
        for i in range(self.r):
            for j in range(self.c):
                self.Update(i,j)
        self.generation += 1
        self.grid = np.copy(self.temp)
        
    
    
    
    def is_valid (self,i,j):
        
        return i>= 0 and j >=0 and i< self.r and j < self.c
        
    def Update(self,i,j):
        
        
        alive = 0 
        dead = 0
        moves = [(-1,1),(1,-1),(1,1),(-1,-1),(0,1),(1,0),(-1,0),(0,-1)]
        
        for k in range(8):
            if self.is_valid(i+moves[k][0],j+moves[k][1]):
                
                if self.grid[i+moves[k][0]][j+moves[k][1]] == 0 :
                    dead += 1 
                    
                else : 
                    alive += 1
        
        if self.grid[i][j] == 0 and alive != 3 :
            self.temp[i][j] = 0
        elif self.grid[i][j] == 1 and (alive > 3 or alive<2) : 
            self.temp[i][j] = 0
        else :
            self.temp[i][j] += 1 
            
    def print_grid (self):
        
        for i in range(self.r):
            for j in range(self.c):
                print(self.grid[i][j],end=" ")
            print(" ")
                        
                    
                
                
        
        
        
    
    
    def start(self):
        print("start life ..............")
        print("initial Grid :")
        self.print_grid()
        x = 1
        while x :
            z = None
            self.check()
            print("Generation no {} :".format(self.generation))
            self.print_grid()
            while not z or z not in "yn" :
                z = input("if you want to see the next Generation enter y if you want to exit enter n \n")
            
                if z == "n" :
                    x = 0
                    print("Good bye")
                elif z!= "y":
                    print("Wrong input try again")

                    

    
    
Game = life()
Game.start()

                
            