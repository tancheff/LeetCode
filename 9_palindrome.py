# Given an integer x, return true if x is a , and false otherwise.

num1 = 121
num2 = -121
num3 = 10


class Solution:
    def is_palindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


solution = Solution()
print(solution.is_palindrome(num1))
