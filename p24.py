def lexico_permutation(s):
    if len(s) == 1: return [s]
    order = []
    for i in s:
        t = s.replace(i,"")
        for j in lexico_permutation(t):
            order.append(i+j)

    return order

print(lexico_permutation("0123456789")[999999])

#Honest to god, im suprised this worked first try lol. 
