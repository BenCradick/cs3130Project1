def fibonacci_recursive(k) :
    if k == 1:
        return 1
    if k == 0:
        return 0
        
    return fibonacci_recursive(k-1)+ fibonacci_recursive(k-2)




results = open("CRAB1A/results.txt", "w")
for k in range (1, 40):
    try:
        result = fibonacci_recursive(k)
        print(f"F({k}) = {result}", file = results)
    except RecursionError:
        print(f"max recursion depth:\t {k-1}", file = results)
        break
results.close()