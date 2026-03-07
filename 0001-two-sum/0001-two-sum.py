class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # i is the index, n is the actual value (nums[i])
        for i, n in enumerate(nums):
            complement = target - n
            if complement in hashmap:
                # We return the current index i and the stored index from the map
                return [i, hashmap[complement]]
            
            # Store the value as the key and its index as the value
            hashmap[n] = i
            
        return []