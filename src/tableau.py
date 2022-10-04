from cmath import inf
import numpy as np
class Tableau():
    def __init__(self,A,b,c):
        self.n=len(c)
        self.m=len(b)
        self.constructTableau(A,b,c)

    def constructTableau(self,A,b,c):
        self.tableau = np.zeros((self.m+1, self.n+self.m+2), dtype=float)
        self.tableau[0:self.m, 0:self.n] = A
        self.tableau[0:self.m, self.n:(self.n+self.m)] = np.identity(self.m)
        self.tableau[0:self.m, (self.n+self.m+1):] = b
        self.tableau[self.m:, 0:self.n] = -c
        self.tableau[self.m ,self.n+self.m] = 1

    def getPivot(self):
        index=np.argmin(self.tableau[self.m,0:self.m+self.n])
        if(self.tableau[self.m,index]>=0):
            return (-1,-1)
        else:
            min=float('inf')
            mini=-1
            for i in range(0,self.m):
                if(self.tableau[i,index]!=0):
                    if(self.tableau[i,self.n+self.m+1]/self.tableau[i,index]<min):
                        min=self.tableau[i,self.n+self.m+1]/self.tableau[i,index]
                        mini=i
            if(mini==-1):
                return (-1,-1)
            else:
                return (mini,index) 
