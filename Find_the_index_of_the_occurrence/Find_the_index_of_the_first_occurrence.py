class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            a1 = haystack.index(needle)
            return a1
        except ValueError:
            return -1
    