import numpy as np
class Tableau():
    def __init__(self,A,b,c):
        self.n=len(c)
        self.m=len(b)
        self.A=A
        self.b=b
        self.c=c
        self.constructTableau()

    def constructTableau(self):
        self.tableau = np.zeros((self.m+1, self.n+self.m+2), dtype=float)
        self.tableau[0:self.m, 0:self.n] = self.A
        self.tableau[0:self.m, self.n:(self.n+self.m)] = np.identity(self.m)
        self.tableau[0:self.m, (self.n+self.m+1):] = self.b
        self.tableau[self.m:, 0:self.n] = -self.c
        self.tableau[self.m ,self.n+self.m] = 1


