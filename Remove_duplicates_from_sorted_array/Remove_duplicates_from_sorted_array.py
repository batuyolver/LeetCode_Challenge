class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    
        index = 0 
        silinecek = []
        while index < len(nums):
            if nums[index] not in silinecek:
                silinecek.append(nums[index])
                index +=1
            else:
                del nums[index]
        return len(nums)
                