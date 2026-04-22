


"""
integer array nums,
return true if you can partition the array into two
sum of the elements in both subsets is equal 

false otherwi---> check if sum % 2 == 0 if not return false 


--> make a set store values 
---> for each iteration add into the stord values and add thoe values in set to 
----->return true if target in dp
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums)//2    

        for i in range(len(nums)-1 ,-1 ,-1):
            nextDp = set()
            for t in dp :
                nextDp.add(t+nums[i])
                nextDp.add(t)
            dp = nextDp
        return True if target in dp else False         

        