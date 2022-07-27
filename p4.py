reversible = 0
for i in range (100,1000):
    # j>= i
    for j in range (i-1,1000):
        strprod = str(i*j)
        if strprod == strprod[::-1] and i*j > reversible:
            reversible = i*j

print(reversible)