from pathlib import Path
from verifier import *
p = Path.cwd() / "inputs/"
class clause:
    def __init__(self,argv):
        self.c1 = int(argv[0])
        self.c2 = int(argv[1])
        self.num1 = abs(self.c1)
        self.num2 = abs(self.c2)
        if (self.c1 > 0 and self.c2 > 0):
            self.func = lambda a,b: a or b
        elif (self.c1 > 0):
            self.func = lambda a,b: a or not b
        elif (self.c2 > 0):
            self.func = lambda a,b: not a or b
        else:
            self.func = lambda a,b: not a or not b

# cycle through files
for file in list(p.rglob("*.txt")):
    file = file.__str__().split("/")[-1]
    filename = "inputs/" + file
    groupnum = file[11:14]
    file = open(filename)
    line = file.readline()
    line = line.split()
    numClauses = int(line[0])
    numInput = int(line[1])
    clauses = {}
    index = 0
    bools = []
    sat = 0
    for i in range(numInput):
        bools.append(1)
    for line in file:
        clauses[index] = clause(line.split(" "))
        a = clauses[index]
        if a.func(bools[a.num1],bools[a.num2]):
            sat += 1
        index += 1
    file.close()


    # output to file
    outputFN = "outputs/output_group" + groupnum + ".txt"
    file = open(outputFN,"w")
    file.write(str(sat))
    for i in range(numInput):
        file.write(str(bools[i]))
    verify(filename,outputFN)
    file.close()