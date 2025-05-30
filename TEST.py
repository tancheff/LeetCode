# list_a = [1, 2, 3, 4, 5]
# offset = 2 # printing from 2nd index onward
#
#
# print(f"Original list: {list_a}")
# print(list_a[offset:])
# print(list_a[:offset])
#
#
# print(list_a[-offset:])
#
#
# words = ["amazon","apple","facebook","google","leetcode"]
#
# for word in words:
#     for letter in word:
#         print(letter)
from collections import Counter

words2 = ["e", "oo"]
subsets = []

# [expression for item1 in iterable1 for item2 in iterable2]

words2_len = len([letter for word in words2 for letter in word])

print(words2_len)

combined_string = "".join(word for word in words2)

print(Counter(combined_string))

print(pow(2, 5)-2)
