# Given two strings ransomNote and magazine, return true if ransomNote can be constructed
# by using the letters from magazine and false otherwise. Each letter in magazine can only be used once in ransomNote.
#
# Examples:
# Input: ransomNote = "a", magazine = "b"
# Output: false
#
# Input: ransomNote = "aa", magazine = "ab"
# Output: false


# print("Helloabc".replace("HE", "", 1))
# exit()

ransom_note = "aa"
magazine = "aab"

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in magazine:
            ransomNote = ransomNote.replace(letter, "", 1)

        if len(ransomNote) > 0:
            return False
        else:
            return True

solution = Solution()
print(solution.canConstruct(ransom_note, magazine))