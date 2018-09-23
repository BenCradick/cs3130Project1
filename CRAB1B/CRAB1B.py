class Fibonacci_Numbers:
    def __init__(self, k):
        ## k represents iterations to perform.
        ## The initial value of k is also the location of the F(k) we are trying to find.
        ## last = F(k-1)
        self.last = 0
        self.current = 1
        self.count = k
    ## F(n) = F(n-1) + F(n-2)s
    def fibonacci_iterative(self) :
        while( self.count > 1 ):
            ##Temporary numbers
            temp = self.current + self.last
            ##Assign F(n) to F(n-1)
            self.last = self.current
            #Calculate next fibonacci number in sequence F(n-2)+F(n-1)
            self.current = temp
            ##decrement counter
            self.count = self.count - 1
        return self.current


results = open("CRAB1B/results.txt", "w")
for k in range (1, 1000):
    try:
        Fib_Num = Fibonacci_Numbers(k)
        result = Fib_Num.fibonacci_iterative()
        print(f"F({k}) = {result}", file = results)
    except RuntimeError:
        
        print(f"max iterative depth:\t {k-1}", file = results)
        break
results.close()