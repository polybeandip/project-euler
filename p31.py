def partition(parts, n):
    if len(parts) == 1:
        if n%parts[0] == 0:
            return 1
        else: return 0

    sum = 0 
    min = parts[0]
    cap = n//min
    21
    for i in range(cap+1):
        sum += partition(parts[1:n+1],n -i*min)

    return sum

print(partition([1,2,5],200))

#not done

