from timeit import default_timer as time_current
##Copy of CRAB1A/B

ITERATIONS = 1
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

def fibonacci_recursive(k) :
    if k == 1:
        return 1
    if k == 0:
        return 0
        
    return fibonacci_recursive(k-1)+ fibonacci_recursive(k-2)


results = open("CRAB1C/results.txt", "w")
print(f"N,Recursive,Iterative", file=results)

## two column matrix stores values that get generated by timeit for each value of F(n) with 1000 runs each
iterative=[0 for x in range(0,40)]
recursive=[0 for x in range(0,40)]
try:
    
    for i in range (1, 41):
            begin = time_current()
            fibonacci_iterative(i)
            end = time_current()
            time = end - begin
            #setup = f"from __main__ import Fibonacci_Numbers;FibNums=Fibonacci_Numbers({i})"
            iterative[i-1] = time

            begin = time_current()
            fibonacci_recursive(i)
            end = time_current()
            time = end - begin


            recursive[i-1] = time
except RecursionError:
    print(i,k)


for k in range (1,41): 
    rec_min = recursive[k-1]
    print(f"{k}, {rec_min}, {iterative[k-1]}", file=results)

    #Results
# N,Recursive,Iterative
# 1, 1.401000190526247e-06, 1.8379942048341036e-06
# 2, 1.6300036804750562e-06, 1.4859979273751378e-06
# 3, 1.4690012903884053e-06, 9.469949873164296e-07
# 4, 2.1089945221319795e-06, 7.580092642456293e-07
# 5, 3.202003426849842e-06, 8.549977792426944e-07
# 6, 5.176989361643791e-06, 9.659997886046767e-07
# 7, 8.293005521409214e-06, 1.0880030458793044e-06
# 8, 1.3266995665617287e-05, 1.2450036592781544e-06
# 9, 2.110200875904411e-05, 1.3870012480765581e-06
# 10, 3.4124008379876614e-05, 1.5200057532638311e-06
# 11, 5.556999531108886e-05, 1.6190024325624108e-06
# 12, 8.907199662644416e-05, 1.7040001694113016e-06
# 13, 0.00014333499711938202, 1.83499651029706e-06
# 14, 0.00023188399791251868, 2.0989973563700914e-06
# 15, 0.00037485100619960576, 2.24300310947001e-06
# 16, 0.0007880850025685504, 2.502987626940012e-06
# 17, 0.001106146999518387, 5.645997589454055e-06
# 18, 0.0015997369919205084, 4.750007065013051e-06
# 19, 0.0028413690015440807, 3.363995347172022e-06
# 20, 0.004057736005051993, 1.1810989235527813e-05
# 21, 0.005220372986514121, 5.470006726682186e-06
# 22, 0.007647810009075329, 4.277011612430215e-06
# 23, 0.014307717006886378, 3.822991857305169e-06
# 24, 0.0225687499914784, 6.693997420370579e-06
# 25, 0.03698160500789527, 4.932997399009764e-06
# 26, 0.05614194400550332, 4.6240020310506225e-06
# 27, 0.08708523299719673, 4.603993147611618e-06
# 28, 0.13668096999754198, 5.135996616445482e-06
# 29, 0.22231512899452355, 4.618996172212064e-06
# 30, 0.3569096970022656, 5.43700298294425e-06
# 31, 0.5992361940006958, 5.116002284921706e-06
# 32, 0.9669125990039902, 5.465990398079157e-06
# 33, 1.5650420649908483, 5.649009835906327e-06
# 34, 2.4540130300010787, 6.62199454382062e-06
# 35, 4.052722029999131, 5.459005478769541e-06
# 36, 6.423913068996626, 5.69300027564168e-06
# 37, 10.512989843002288, 5.829992005601525e-06
# 38, 17.71152117800375, 6.050002411939204e-06
# 39, 27.398422776008374, 6.580987246707082e-06
# 40, 44.98877002799418, 6.280999514274299e-06
