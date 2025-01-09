from typing import List

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

list_a = [3,1,2,10,1]


class Solution:
    def running_sum(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(0, len(nums)):
            sum = 0

            for j in range(0, i+1):
                sum += nums[j]

            result.append(sum)

        return result

solution = Solution()
print(solution.running_sum(list_a))


"""
faster solution:

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        running_sums = [nums[0]]
        for i in range(1, n):
            running_sums.append(nums[i] + running_sums[-1])
        
        return running_sums

"""
