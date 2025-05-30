# Given a signed 32 - bit integer x,return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range[-231, 231 - 1],
# then return 0.
#
# Example:
# Input: x = 123
# Output: 321


class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = pow(-2, 31), pow(2, 31) - 1

        if x == 0:
            return 0

        num_as_str = str(x)
        result = ""

        for i in range(len(num_as_str) - 1, -1, -1):
            if num_as_str[i] == "0":
                if result == "":
                    continue

            if num_as_str[i] == "-":
                result = "-" + result
                break

            result += num_as_str[i]

        if not INT_MIN <= int(result) <= INT_MAX:
            return 0

        return int(result)


solution = Solution()

print(solution.reverse(123))        # Result: 321
print(solution.reverse(-123))       # Result: -321
print(solution.reverse(120))        # Result: 21
