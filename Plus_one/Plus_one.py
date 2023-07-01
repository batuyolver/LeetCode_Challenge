class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_list = [str(x) for x in digits]
        digit_list2 = ""
        for x in digits_list:
            digit_list2 = digit_list2 + x
        digit_list3 = int(digit_list2)

        if len(digits) == 1 or digit_list3%10 == int(digit_list2[-1]):
            plus_two = 1
        else:
            if min(digits) == 0:
                plus_two = 1
            else:
                plus_two = min(digits)

        new_value = str(digit_list3 + plus_two)
        new_value = [int(x) for x in new_value]
        return new_value