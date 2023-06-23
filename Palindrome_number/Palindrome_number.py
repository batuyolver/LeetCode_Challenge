class Solution:
    def isPalindrome(self, x: int) -> bool:
        source = x
        new_list = []
        while (source >0):
            digit = source %10
            source //= 10
            new_list.append(digit)
        counter = 1
        son_sayi = 0
        for y in new_list:
            son_sayi = son_sayi + (y * (10**(len(new_list)-counter)))
            counter +=1
        son_sayi == int(son_sayi)
        if son_sayi == x:
            return True
        else:
            return False