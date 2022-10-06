from src.tableau import *
import numpy as np

class LinearProgram():
    def __init__(self):
        self.takeInput()
        self.tableau = Tableau(self.matrixA, self.matrixB, self.c)
        self.solution = None

    def takeInput(self):
        print("Do you wish to maximise (Y) or minimize (N) the cost function?")
        isMax=input()
        if(isMax.upper()=='Y'):
            self.multiplier=1
        else:
            self.multiplier=-1
        print("Enter the coefficients of the cost function (space separated in a line)")
        self.c=[float(i)*self.multiplier for i in input().split()]
        self.c=np.array(self.c)
        n=len(self.c)

        #inputting the equations for Ax<=b
        print("Taking inputs for constraints Ax<=b in the form a1x1+a2x2+.....anxn<=b")
        self.matrixA=[]
        self.matrixB=[]
        while(True):
            print("Enter n coefficients of the constraint equation")
            a=[float(i) for i in input().split()]
            if(len(a)==n):
                self.matrixA.append(a)
                print("Enter the value of b")
                b=float(input())
                self.matrixB.append([b])
            else:
                print("Incorrect number of coefficients, please try again")
            print("Do you wish to continue?(Y/N)")
            choice=input()
            if(choice.upper()=='N'):
                break

        self.matrixA=np.array(self.matrixA)
        self.matrixB=np.array(self.matrixB)

    def solve(self):
        while(True):
            pivot = self.tableau.getPivot()
            if(pivot == (-2, -2)):
                #Recursion Over, Now solve Linear Equations
                break   
            if(pivot == (-1, -1)):
                #Solution is INF
                self.solution = float('inf')
                break 
            self.tableau.gaussTransform(pivot)
            
    def getSoln(self):
        if(self.solution == float('inf')):
            print("Cost function is unbounded!")
            return
        print(self.tableau.tableau)


