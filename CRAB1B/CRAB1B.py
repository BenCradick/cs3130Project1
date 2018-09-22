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

fib_nums = Fibonacci_Numbers(10)
print(fib_nums.fibonacci_iterative())