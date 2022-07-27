import math

def divisor_count(n):
    i=2
    prod =1 
    while n != 1:
        count = 0
        while n % i == 0:
            count += 1
            n = n/i
        prod *= count + 1
        i = i+1

    return prod
            
        
n=1
while True:
    if divisor_count(n*(n+1)/2) > 500:
        print(n*(n+1)/2)
        break

    n += 1

