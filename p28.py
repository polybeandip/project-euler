# more bashing

count = 0
for i in range(2,502):
    odd = 2*i - 1
    count += (odd**2) + (odd**2 - odd +1) + (odd**2 - 2*odd + 2) + (odd**2 - 3*odd + 3)

print(count + 1)

