# You are given two string arrays words1 and words2.
# A string b is a subset of string a if every letter in b occurs in a including multiplicity.
#
# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.
# Return an array of all the universal strings in words1. You may return the answer in any order.
#
# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
# Output: ["facebook","google","leetcode"]
from collections import Counter

words1 = ["amazon", "apple","facebook","google","leetcode"]
# words1 = ["leetcode"]  # Expected: ["google","leetcode"]
words2 = ["lo","eo"]

subsets = []
w2_combined = "".join(word for word in words2)
w2_counter = Counter(w2_combined)

#nested list comprehension
# [expression for item1 in iterable1 for item2 in iterable2]
words2_len = len(w2_counter)

for word1 in words1:
    counter_for_matches = 0
    w1_counter = Counter(word1)

    for word2 in words2:
        w2_counter = Counter(word2)

        for key1, val1 in w1_counter.items():
            for key2, val2 in w2_counter.items():
                if key1 == key2 and val1 >= val2:
                    counter_for_matches += 1
                    if counter_for_matches == words2_len:
                        subsets.append(word1)
                        break
            if counter_for_matches == words2_len:
                break
        if counter_for_matches == words2_len:
            break

print(subsets)
