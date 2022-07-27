from math import sqrt

def divisor_sum(n):
    sum = 0
    for i in range(1,n):
        if n %i == 0: sum += i
    
    return sum

amicable_sum = 0
for i in range(1,10000):
    if i == divisor_sum(divisor_sum(i)) and divisor_sum(i) != i:
        amicable_sum += i   

print(amicable_sum)