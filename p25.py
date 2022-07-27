def fib(n):
    count = 1
    x = 0
    y = 1
    while count< n:
        (x,y) = (x+y,x+2*y)
        # print(x)
        # print(y)
        count += 2

    if n % 2 == 0: return x
    else: return y

i = 0
while True:
    if len(str(fib(i))) == 1000: 
        print(i)
        break

    i += 1

