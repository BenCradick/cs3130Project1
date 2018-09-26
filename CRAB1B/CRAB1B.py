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
for k in range (1, 50):
    try:
        
        result = fibonacci_iterative(k)
        print(f"F({k}) = {result}", file=results)
    except RuntimeError:
        
        print(f"max iterative depth:\t {k-1}", file = results)
        break
results.close()
#Results
# F(1) = 1
# F(2) = 1
# F(3) = 2
# F(4) = 3
# F(5) = 5
# F(6) = 8
# F(7) = 13
# F(8) = 21
# F(9) = 34
# F(10) = 55
# F(11) = 89
# F(12) = 144
# F(13) = 233
# F(14) = 377
# F(15) = 610
# F(16) = 987
# F(17) = 1597
# F(18) = 2584
# F(19) = 4181
# F(20) = 6765
# F(21) = 10946
# F(22) = 17711
# F(23) = 28657
# F(24) = 46368
# F(25) = 75025
# F(26) = 121393
# F(27) = 196418
# F(28) = 317811
# F(29) = 514229
# F(30) = 832040
# F(31) = 1346269
# F(32) = 2178309
# F(33) = 3524578
# F(34) = 5702887
# F(35) = 9227465
# F(36) = 14930352
# F(37) = 24157817
# F(38) = 39088169
# F(39) = 63245986
# F(40) = 102334155
# F(41) = 165580141
# F(42) = 267914296
# F(43) = 433494437
# F(44) = 701408733
# F(45) = 1134903170
# F(46) = 1836311903
# F(47) = 2971215073
# F(48) = 4807526976
# F(49) = 7778742049