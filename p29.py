nums = set()

for a in range(2,101):
    for b in range(2,101):
        if a**b not in nums:
            nums.add(a**b) 

print(len(nums))

# what was the point of this problem???