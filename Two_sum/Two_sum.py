class Solution:
    def twoSum(self,nums: List[int], target: int) -> List[int]:
        final = []
        for x in range(len(nums)):
            search = nums[x]
            for y in range(x+1, len(nums)):
                search_2 = nums[y]
                if search + search_2 == target:
                    final.append(x)
                    final.append(y)
        return final

