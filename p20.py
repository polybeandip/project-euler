prod = 1
for i in range(1,101):
    prod = prod*i

prodstring = str(prod)

sum = 0
for i in prodstring:
    sum += int(i)

print(sum)