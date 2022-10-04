from sys import stdin
from tableau import *
import numpy as np

if __name__=="__main__":
    print("Do you wish to maximise (Y) or minimize (N) the cost function?")
    maxOrMin=input()
    if(maxOrMin.upper()=='Y'):
        multiplier=1
    else:
        multiplier=-1
    print("Enter the coefficients of the cost function (space separated in a line)")
    c=[float(i)*multiplier for i in input().split()]
    c=np.array(c)
    n=len(c)

    #inputting the equations for Ax<=b
    print("Taking inputs for constraints Ax<=b in the form a1x1+a2x2+.....anxn<=b")
    matrixA=[]
    matrixB=[]
    while(True):
        print("Enter n coefficients of the constraint equation")
        a=[float(i) for i in input().split()]
        if(len(a)==n):
            matrixA.append(a)
            print("Enter the value of b")
            b=float(input())
            matrixB.append([b])
        else:
            print("Incorrect number of coefficients, please try again")
        print("Do you wish to continue?(Y/N)")
        choice=input()
        if(choice.upper()=='N'):
            break

    matrixA=np.array(matrixA)
    matrixB=np.array(matrixB)
    
    tableau = Tableau(matrixA, matrixB, c)


