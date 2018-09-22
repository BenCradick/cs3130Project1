def fibonacci_recursive(k, current, last) :
    if k > 1 : 
        temp = current + last    
        k = k - 1
        return fibonacci_recursive(k, temp, current)
    else : 
        return current

def fib_helper(k) :
    return fibonacci_recursive(k, 1, 0)

print(fib_helper(10))