def cancel(a,b):
    val = a/b
    for i in [0,1]:
        for j in [0,1]:
            if str(b)[j] == "0":
                continue
            if int(str(a)[i])/int(str(b)[j]) == val and str(b)[1-j] == str(a)[1-i]:
                return True

    return False

nume = 1
denom = 1

for i in range(11,99):
    for j in range(i+1,99):
        if not (i%10 == 0 and j%10 == 0) and cancel(i,j):
            nume *= i
            denom *= j

from fractions import Fraction

print(Fraction(nume, denom))
