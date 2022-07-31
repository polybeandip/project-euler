from math import log10
#checks if a given set of three numbers covers all the digits from 1-9 exactly once
def special(a,b,c):
    digits = []
    for i in [a,b,c]:
        while i > 0:
            if i%10 in digits or len(digits) > 9 or i%10 == 0: return False
            else:
                digits.append(i%10)
                i = i//10
    if len(digits) == 9 and 0 not in digits: return True
    else: return False

count = 0
works = set()

for i in range(1,100000):
    for j in range(i, int(10**(5 - log10(i) + 1))):
        if special(i,j, i*j) and i*j not in works:
            count = count + i*j
            works.add(i*j)
        
print(count) 

