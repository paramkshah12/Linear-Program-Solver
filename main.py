from src.simplex import *

if __name__=='__main__':
    lp=LinearProgram()
    lp.solve()
    lp.getSoln()