# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
from typing import List

strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        prefix = ""

        shortest_word = min([len(s) for s in strs])

    # TO DO: fix nested loop!

        for i in range(0, shortest_word):
            prefix += strs[0][i]
            for j in range(0, len(strs)):
                if prefix[i] != strs1[i][j]:
                    return prefix


        return prefix


solution = Solution()
print(solution.longest_common_prefix(strs1))
