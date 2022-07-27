def collatz_counter(n):
    count = 0
    while n != 1:
        if n % 2 == 0: 
            n = n/2
            count += 1
        else: 
            n = 3*n + 1
            count += 1
    return count

max = 0
maxnum = 1
for i in range(1,1000000):
    if max < collatz_counter(i): 
        max = collatz_counter(i)
        maxnum = i

print(maxnum)
#pure bash