"""
Authors: David Zomerdijk, Maurits Bleeker
"""
from sympy.solvers import solve
from sympy import Symbol

#prints the pay-off matrix in the console
def printMatrix(matrix, name):
    print("\nPay-off Matrix of", name , ":")
    print("       C       D")
    print("C  ", matrix[0][0], " ",matrix[0][1]  )
    print("D  ", matrix[1][0], " ",matrix[1][1]  , "\n")

#finds the pure nash equilibria
def findPure(matrix):
    noNash = True
    coordinatesDict ={ (0,0) : "CC", (0,1) : "CD", (1,0) : "DC" , (1,1): "DD" }

    #checks whether a position in the matrix is pure
    def isPureNash(matrix, c ):
        NE = False
        row_utility         = matrix[ c[0] ][ c[1] ][0]
        column_utility      = matrix[ c[0] ][ c[1] ][1]

        row_utility_alt     = matrix[ int( not c[0]) ][ c[1]           ][0]
        column_utility_alt  = matrix[ c[0]           ][ int(not c[1])  ][1]

        #checks for both rows and columns if there is a better strategy available
        if row_utility >= row_utility_alt and column_utility >= column_utility_alt:
            NE = True

        return NE

    #print the pure nash equilibria, otherwise say there aren't any.
    for key, value in coordinatesDict.items():
        if isPureNash(matrix, key):
            print(value, " is a pure Nash equilibrium.")
            noNash = False
    if noNash:
        print("There are no pure Nash equilibria in this game.")


#finds all mixed equilibria of a matrix
def findMixed(m):
    x = Symbol('x')
    #column indifferent when:
    p = solve(m[0][0][1] * x + m[1][0][1]*( 1 - x) - ( m[0][1][1]* x + m[1][1][1]*(1-x)), x)[0]
    #above I use a solver that basically does the same as we did in homework one.

    #row indifferent when:
    q = solve(m[0][0][0]* x  + m[0][1][0] *( 1 - x) - ( m[1][0][0]* x + m[1][1][0]*(1-x)), x)[0]

    #underneath we print the solutions.
    if p not in [0,1] and q not in [0,1]:
        print("The mixed equilibrium is: (("  + str(p)  + ", " + str(1- p) + "), (" + str(q) + ", " + str(1-q) +"))")
    #in the case either p or q is 1 or 0 we know that there is a range of NE. These are printed below.
    else:
        if (p == 1 or p ==0) and q < 0.5:
            print("The mixed equilibria are: ((" + str(p) + ", " + str(1 - p) + "), (" + "q" + ", " + "1 - q" + "))")
            print("Where q is in [0, " + str(q)+"]." )
        elif (p == 1 or p == 0) and q > 0.5:
            print("The mixed equilibria are: ((" + str(p) + ", " + str(1 - p) + "), (" + "q" + ", " + "1 - q" + "))")
            print("Where q is in [" + str(q)+", 1]." )
        elif (q == 1 or q==0) and p < 0.5:
            print("The mixed equilibria are: ((" + "q" + ", " + "1-q" + "), (" + str(q) + ", " + str(1-q) + "))")
            print("Where p is in [0," + str(p)+" ]." )
        elif(q == 1 or q==0) and p > 0.5:
            print("The mixed equilibria are: ((" + str(p) + ", " + str(1 - p) + "), (" + "q" + ", " + "1 - q" + "))")
            print("Where p is in [" + str(p)+", 1].")
        #in case we find a pure nash equilibrium we just print int as well.
        else:
            print("The mixed equilibrium turns out to be a pure NE: ((" + str(p) + ", " + str(1 - p) + "), (" + str(q) + ", " + str(
                1 - q) + "))")

#This function takes a matrix and prints the pay-off matrix and finds alls NE's.
def findAllNash(matrix,name="Example") :
    printMatrix(matrix,name)
    findPure(matrix)
    findMixed(matrix)


#beneath we run our functions
if __name__ == "__main__":

    ##first example-----------------------------
    example1 = [[(5, 8), (3, 4)],
               [ (2, 2), (7, 3)]]

    findAllNash(example1, "example1")

    ##second example----------------------------
    example2 = [[(2, 3), (5, 3)],
               [ (5, 4), (3, 3)]]

    findAllNash(example2, "example2")

    ##third example-----------------------------
    example3 = [[(1, 2), (2, 1)],
               [ (2, 1), (1, 2)]]

    findAllNash(example3, "example3")

    ##fourth example----------------------------
    example4 = [[(5, 3), (2, 3)],
               [ (3, 4), (5, 3)]]

    findAllNash(example4, "example4")





