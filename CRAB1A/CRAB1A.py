class Fibonacci_Numbers:
    def __init__(self, k):
        ## k represents recursions remaining.
        ## The initial value of k is also the location of the F(k) we are trying to find.
        ## last = F(k-1)
        self.last = 0
        ## penultimate = F(k-2) 
        ## NOTE: Penultimate means second to last in English.
        self.penultimate = 0
        self.current = 1
        self.recursions = k
    ## F(n) = F(n-1) + F(n-2)s
    def fibonacci_recursive() :
        ##Temporary numbers
        temp = self.current
        #Calculate next fibonacci number in sequence F(n-2)+F(n-1)
        self.current = self.last + self.penultimate
        self.penultimate = self.FitNumbers.last
        self.last

