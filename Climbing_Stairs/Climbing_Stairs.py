class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1 
        general_list = [1,2]
        for x in range(1,n-1):
            general_list.append(general_list[x] + general_list[x-1])
    
        return general_list[-1]