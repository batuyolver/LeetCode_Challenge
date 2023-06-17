class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = s
        if len(string) == 0:
            return 0
        a = 0
        k = 1
        sub = string[0]
        len_list = []
        while a < len(string) and a+k < len(string):
            sub = sub + string[a+k]
            if sub.count(string[a+k]) != 1:
                len_list.append(len(sub)-1)
                sub = ""
                a+=1
                k= 0
            else:
                k+=1
        len_list.append(len(sub))
        if len(len_list) == 0:
            return 1
        return max(len_list)