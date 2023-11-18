t = input()

data = []

class testCase:
    def __init__(self, numTowers, towerPowers, towerDistances):
        self.numTowers = numTowers
        self.towerPowers = towerPowers
        self.towerDistances = towerDistances

def checkAllIsEqualExceptOne(ls):
    count = len(ls)
    for x in range(ls):
        if x == ls[0]:
            count += 1
    if count >= len(ls) - 1:
        return True
    else:
        return False


def findMinTime(n, p, d): #minimum time to destroyu all given a the tower data
    
    timesForStartTowers = []
    for startTowerIndex in range(len(p)): # cycle through starting towers so we calc each one
        log = [0 for _ in range(len(p))]
        for index in range(p)
            hours = 0
            hpower = 0

            if hpower >= p[startTowerIndex + index]:
                log[startTowerIndex + index]

            hours, hpower += 1

            
        


for x in range(int(t) *3):
    data.append([int(y) for y in input().split()]) 

testCases = []

for index in range(len(data)):
    if (index+1 % 3 == 0) or index == 0: #if the current data is numtowers
        testCases.append(testCase(data[index], data[index+1], data[index+2]))



