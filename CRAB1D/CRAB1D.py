class BigIntFibonacci:
    def __init__(self):
        self.previous = [0 for x in range(0,99)]
        self.penultimate = [0 for x in range(0,99)]
        self.current = [0 for x in range(0,100)]
        self.previous[0] = 1
        self.current[0] = 1
        self.N = 0

    def addTwoCells(self,location):
        if self.previous[location] + self.penultimate[location] + self.current[location] >= 10:
            self.current[location + 1] += 1
            temp = self.current[location] + self.previous[location] + self.penultimate[location]
            temp %= 10
            self.current[location] = temp
        else:
            self.current[location] += self.previous[location]
            self.current[location] += self.penultimate[location]
    
    def reset(self):
        self.penultimate = [0 for x in range(0,100)]
        self.penultimate = self.previous.copy()
        self.previous = [0 for x in range(0,100)]
        self.previous = self.current.copy()
        self.current = [0 for x in range(0,100)]

    def calcCurrent(self):
        for loc in range(0,99):
            self.addTwoCells(loc)

    def findMax99digitFib(self):
        while self.current[99] == 0:
            self.reset()
            self.calcCurrent()
        self.printBigInt()
    def printBigInt(self):
        result = open("CRAB1D/results.txt", "w")
        formatted = " "
        for x in range(0,99):
            if x%3 == 0:
                formatted+=","
            formatted+=str(self.previous[99-x])
        print(f"Last 99 digit integer found", file = result)
        print(f"{formatted[3:len(formatted)]}", file=result)
FibNums = BigIntFibonacci()
FibNums.findMax99digitFib()

#Results
#Last 99 digit integer found
#83,108,245,990,870,293,529,395,578,470,112,099,370,436,902,820,065,161,385,997,283,008,073,998,054,106,554,467,481,203,415,169,952


    


    