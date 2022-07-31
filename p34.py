def factorial(n):
    prod = 1
    for i in range(1,n+1):
        prod = prod * i

    return prod

saved = {}
for i in range(0,10):
    saved[i] = factorial(i) 


def digit_factorial(n):
    og = n
    d = n % 10
    sum = 0
    while n > 0:
        sum += saved[d] 
        n = n//10
        d = n % 10

    if sum == og: return True
    else: return False

sum = 0

for n in range(3,1000000):
    if digit_factorial(n) == True:
        sum += n

print(sum) 

#currently don't have a good reason for why I stopped at a million. It works though ¯\_()_/¯. Maybe I'll writeup a reason later
