from pathlib import Path
from verifier import *
p = Path.cwd() / "inputs/"
class clause:
    def __init__(self,argv):
        self.c1 = int(argv[0])
        self.c2 = int(argv[1])
        self.num1 = abs(self.c1) - 1
        self.num2 = abs(self.c2) - 1
        if (self.c1 > 0 and self.c2 > 0):
            self.func = lambda a,b: a or b
        elif (self.c1 > 0):
            self.func = lambda a,b: a or not b
        elif (self.c2 > 0):
            self.func = lambda a,b: not a or b
        else:
            self.func = lambda a,b: not a or not b

def algo(bools,clauses):
    falses = []
    falseClauses = {}
    sat = 0
    for i in range(len(bools)):
        falseClauses[i] = 0
    for i in range(len(clauses)):
        c = clauses[i]
        if not c.func(bools[c.num1],bools[c.num2]):
            falses.append(i)
            if c.c1 < 0:
                falseClauses[c.num1] += 1
            elif c.c2 < 0:
                falseClauses[c.num2] += 1
        else:
            # if c.c1 > 0:
            #     falseClauses[c.num1] -= 1
            # if c.c2 > 0:
            #     falseClauses[c.num2] -= 1
            sat += 1
    for i in range(len(bools)):
        newSat = 0
        if falseClauses[i] > 0:
            if bools[i] == 0:
                bools[i] = 1
            else:
                bools[i] = 0
            for j in range(len(clauses)):
                a = clauses[j]
                if a.func(bools[a.num1],bools[a.num2]):
                    newSat += 1
            if (newSat > sat):
                sat = newSat
            elif bools[i] == 0:
                bools[i] = 1
            else:
                bools[i] = 0


    return bools,clauses
    
    

# cycle through files
for file in list(p.rglob("*63.txt")):
    file = file.__str__().split("/")[-1]
    filename = "inputs/" + file
    print("Running " + filename + "...")
    groupnum = file[11:14]
    file = open(filename)
    line = file.readline()
    line = line.split()
    numClauses = int(line[0])
    numInput = int(line[1])
    clauses = {}
    index = 0
    bools = [-1 for i in range(numInput)]
    sat = 0
    A = open("a.txt",'w')
    b = open("b.txt",'w')
    for line in file:
        clauses[index] = clause(line.split(" "))
        index += 1
    for i in range(numInput):
        bools[i] = 1
    #     c = clauses[i]
    #     if (c.c1 < 0):
    #         bools[c.num1] = 0
    #     elif (c.c1 > 0 and c.c2 < 0):
    #         bools[c.num2] = 0
    # for i in range(numInput):
    #     if (bools[i] == -1):
    #         bools[i] = 1

    bools,clauses = algo(bools,clauses)

    for i in range(numClauses):
        a = clauses[i]
        if a.func(bools[a.num1],bools[a.num2]):
            b.write(str(bools[a.num1]) + str(bools[a.num2]) + "\n")
            sat += 1
        else:
            A.write(str(bools[a.num1]) + str(bools[a.num2]) + "\n")
    file.close()
    A.close()
    b.close()


    # output to file
    outputFN = "outputs/output_group" + groupnum + ".txt"
    file = open(outputFN,"w")
    file.write(str(sat) + "\n")
    for i in range(numInput - 1):
        file.write(str(bools[i]) + "\n")
    file.write(str(bools[-1]))
    file.close()
    verify(filename,outputFN)