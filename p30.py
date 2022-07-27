sum = 0
for i in range(2,1000000):
    num_string = str(i)
    s = 0
    for j in num_string:
        s += int(j)**5

    if s == i: 
        sum += i

print(sum)

# the sum of the fifth powers of an n digit number is bouned above by 9^5 * n. For n = 7, notice 7 * 9^5 < 10^6. It's easy to induct and show n * 9^5 < 10^n-1 for all n > 5. Hence, we need only till the 6th digit numbers for this problem 