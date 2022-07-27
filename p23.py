def is_abundant(n):
    sum = 0
    for i in range(1,n//2 + 1):
        if n % i == 0:
            sum += i

    return sum > n

abundant = []
for i in range(1,28124):
    if is_abundant(i): abundant.add(i)

#apparently checking if something is in a set is way quicker than with a list for some reason
abundant_sum = set([])
not_abundant = 0  

for i in abundant:
    for j in abundant:
        if i + j > 28123:
            break
        else:
            abundant_sum.add(i+j)

NonAbSums = [number for number in range(28124) if number not in abundant_sum]

print(sum(NonAbSums)) 

