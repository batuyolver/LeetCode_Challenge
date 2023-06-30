class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string1 = s.split(" ")
        string1 = string1[::-1]
        for x in string1:
            if len(x) !=0:
                return len(x) 