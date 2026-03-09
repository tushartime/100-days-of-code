class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        # We start at 1 to compare backward safely
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False