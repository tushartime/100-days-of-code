from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 1. Correct the capitalization: 'collections', not 'Collections'
        counts = Counter(nums)
        index = 0

        # 2. Fix indentation: Everything inside the function must line up
        for color in [0, 1, 2]:
            # 3. Repeat based on how many times that color appeared
            for _ in range(counts[color]):
                # 4. Modify the original list 'nums' at the current 'index'
                nums[index] = color
                index += 1