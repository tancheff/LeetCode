# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

nums = [-4,-1,0,3,10]
squares = []

for num in nums:
    squares.append(num**2)

print(sorted(squares))