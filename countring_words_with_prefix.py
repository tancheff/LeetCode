# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
# A prefix of a string s is any leading contiguous substring of s.
#
# Input: words = ["pay","attention","practice","attend"], pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
from typing import List

words = ["pay","attention","practice","attend"]
pref = "at"

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pref_len = len(pref)
        words_with_prefix = []

        for word in words:
            if len(word) >= pref_len:
                if word[:pref_len] == pref:
                    words_with_prefix.append(word)

        return len(words_with_prefix)
