class Solution:
    def maxProduct(self, nums: List[int]) -> int:
       
        leftproduct = 1
        rightproduct = 1
        ans = nums[0]

        for i in range(len(nums)):

            if leftproduct == 0 : leftproduct=1
            if rightproduct == 0 : rightproduct=1

            #prefix
            leftproduct *= nums[i]
            #suufix
            rightproduct *= nums[len(nums)-1-i] 

            ans = max(ans,max(leftproduct,rightproduct))
        return ans    
        