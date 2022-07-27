file = open("namesforp22.txt", "r")

names = file.read().split(",")

for (i,val) in enumerate(names):
    names[i] = val.strip('"')

names.sort()

def score(s):
    score = 0
    Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in s:
        score += Letters.index(i) + 1
    return score

total = 0
for (i,val) in enumerate(names):
    total += score(val)*(i+1)

print(total)
