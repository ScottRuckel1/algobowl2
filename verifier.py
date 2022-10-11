import readline
from signal import valid_signals
def verify(s,s1):
    inFile = open(s)
    outFile = open(s1)
    varValues = []
    # Output file
    
    truesClaimed = int(outFile.readline())
    for line in outFile:
        varValues.append(int(line))

    # Input file 
    line = inFile.readline()

    for line in inFile:
        line = line.split()
        num1 = int(line[0])
        num2 = int(line[1])
        bool1 = varValues[abs(num1)]
        bool2 = varValues[abs(num2)]
        if ((num1 < 0 and not bool1) or
            (num2 < 0 and not bool2) or
            (num1 > 0 and bool1) or
            (num2 > 0 and bool2)):
            truesClaimed -= 1
    if truesClaimed != 0:
        print("Trues claimed does not match")
        return 0
    print("Passed verification")
    return 1