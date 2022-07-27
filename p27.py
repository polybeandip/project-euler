from math import sqrt

# prime check
def is_prime(n):
    i = 2
    if sqrt(n).is_integer() == True: return False
    while i <= sqrt(n):
        if n %i == 0: return False
        i+= 1

    return True

def quad(a,b,n):
    return abs(n**2 + a*n + b)

# now we bash
max = 0
amax = 0
bmax = 0
for a in range(-1000,1001):
    for b in range(-1000,1001):
        n=0
        length = 0
        
        while is_prime(quad(a,b,n)) == True:
            length += 1
            n+= 1
        
        if length > max : 
            max = length
            amax, bmax = a,b

print(amax * bmax)