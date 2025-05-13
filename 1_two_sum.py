# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [3,2,4]
target = 6
answer = []

for i in range(len(nums)-1):
    num_1 = nums[i]

    for j in range(i+1, len(nums)):
        num_2 = nums[j]

        if num_1 + num_2 == target:
            # answer.extend((num_1, num_2))
            answer.extend((i, j))
            break

    if len(answer) > 0:
        break

print(answer)