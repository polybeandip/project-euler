x = 1
y = 2

sum = 0

while y < 4000000:
    sum += y
    newy = 3*y + 2*x
    newx = 2*y + x

    y = newy
    x = newx

print(sum)
