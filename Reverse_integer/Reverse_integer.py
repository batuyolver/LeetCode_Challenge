class Solution:
    def reverse(self, x: int) -> int:
        number = x
        number_one = number
        if number <0:
            number = abs(number)
    
        new_list = []
    
        while number > 0:
            digit = number %10
            number //= 10
            new_list.append(digit)
        new_number = 0
        counter = 1
        for a in new_list:
            new_number = new_number + a * (10**(len(new_list)-counter))
            counter +=1
    
        if number_one <0:
            new_number = -new_number
        if new_number >= -(2**31) and new_number <= (2**31-1):
            return new_number
        else:
            return 0