class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = []
        
        for x in nums1:
            new_list.append(x)
        for y in nums2:
            new_list.append(y)
        
        new_list.sort()
        
        if len(new_list) %2 !=0:
            median = new_list[len(new_list)//2]
        
        if len(new_list) %2==0:
            median = (new_list[(len(new_list)//2)-1] + new_list[len(new_list)//2]) /2
        
        return median