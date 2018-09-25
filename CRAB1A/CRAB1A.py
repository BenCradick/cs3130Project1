def fibonacci_recursive(k, current, last) :
    if k > 1 : 
        temp = current + last    
        k = k - 1
        return fibonacci_recursive(k, temp, current)
    else : 
        return current




results = open("CRAB1A/results.txt", "w")
for k in range (1, 1000):
    try:
        result = fibonacci_recursive(k, 1, 0)
        print(f"F({k}) = {result}", file = results)
    except RecursionError:
        print(f"max recursion depth:\t {k-1}", file = results)
        break
results.close()