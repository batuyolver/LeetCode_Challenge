class Solution:
    def maxArea(self, height: List[int]) -> int:
        lst = height
        left = 0 
        right = len(lst)-1 
        max_area = 0 
        while left < right:
            max_area = max(max_area, min(lst[left], lst[right])* (right-left))
            if lst[left] < lst[right]:
                left +=1
            else:
                right -=1
    
        return max_area