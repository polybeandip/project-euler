n = 600851475143
p = 2

while n != 1:
    if n % p == 0:
        while n %p == 0:
            n = n/p

    p = p+1

print(p-1)