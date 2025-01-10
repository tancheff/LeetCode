# Given a binary array nums, return the maximum number of consecutive 1's in the array.
nums = [1,1,0,1,1,1]
max = 0
count = 0

for num in nums:
    if num == 1:
        count += 1
        if count > max:
            max = count

    if num != 1:
        count = 0

print(max)