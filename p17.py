ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

oneto19 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

sum = 0

# 1 to 19
for i in oneto19:
    sum += len(i)

# 20 to 99
for i in tens:
    for j in ones:
        sum += len(i + j)

sumlessthan100 = sum

#100 to 999 minus multiples of 100
for i in ones:
    if i == "": continue
    sum += (len(i) + len("hundredand"))*99 + sumlessthan100

#multiples of onehundred
for i in ones:
    if i == "": continue
    sum += len(i) + len("hundred")

sum += len("onethousand")

print(sum)