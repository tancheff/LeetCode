# Given a roman numeral, convert it to an integer.

s1 = "III"
s2 = "LVIII"
s3 = "MCMXCIV"


class Solution:
    VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'None': 0
    }

    def roman_to_int(self, s: str) -> int:
        num = 0
        for i in range(0, len(s)):
            char = s[i]
            next_char = s[i + 1] if i+1 < len(s) else 'None'
            if self.VALUES[next_char] > self.VALUES[char]:
                num -= self.VALUES[char]
                continue

            num += self.VALUES[char]

        return num


solution = Solution()
print(solution.roman_to_int(s3))
