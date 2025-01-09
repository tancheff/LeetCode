# Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
#
# isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.
# For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.
#
# Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

# сравняваме всеки стринг с всички останали

# words = ["a","aba","ababa","aa"]
words = ["a","abb"]

pairs = 0

for i in range(0, len(words)-1):
    for j in range(i+1, len(words)):
        prefix = words[i]
        prefix_len = len(prefix)
        if len(words[j]) >= prefix_len:
            if words[j][:prefix_len] == prefix and words[j][-prefix_len:]== prefix:
                pairs += 1

print(pairs)