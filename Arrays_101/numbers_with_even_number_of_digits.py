# Given an array nums of integers, return how many of them contain an even number of digits.
nums = [12,345,2,6,7896]
count = 0

for num in nums:
    if len(str(num)) % 2 == 0:
        count += 1

print(count)