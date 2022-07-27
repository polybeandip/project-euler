import math

for i in range(1,1000):
    for j in range(i,1000):
        if i + j + math.sqrt(i**2 + j**2) == 1000:
            print(i*j*math.sqrt(i**2 + j**2))