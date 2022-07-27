primes = [2,3,5,7,11,13,17,19]
n = 20
ans = 1

for i in primes:
    j = 0
    while i**j < n:
        j += 1
    ans = ans * i**(j-1)

print(ans)
