import math
bigprod = 2
p = 3
count = 1

while count < 10001:
    if math.gcd(bigprod,p) == 1:
        bigprod *= p
        count += 1
    p += 1

print(p-1)