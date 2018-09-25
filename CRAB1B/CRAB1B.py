def fibonacci_iterative(k) :
    penultimate = 0
    last = 0
    current = 1
    while( k > 1 ):
        penultimate = last
        #Calculate next fibonacci number in sequence F(n-2)+F(n-1)
        last = current
        ##Temporary numbers
        current = last + penultimate
        ##Assign F(n) to F(n-1)
        
        #print(k, current)
        ##decrement counter
        k -= 1
    return current

results = open("CRAB1B/results.txt", "w")
for k in range (1, 1000):
    try:
        
        result = fibonacci_iterative(k)
        print(f"F({k}) = {result}", file=results)
    except RuntimeError:
        
        print(f"max iterative depth:\t {k-1}", file = results)
        break
results.close()