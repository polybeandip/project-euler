import math

# prime checker
def pcheck(n):
    if n == 1: return False
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0: return False
        i = i+1 

    return True

sum = 0

for i in range(2000000):
    if pcheck(i) == True: 
        sum += i

print(sum)