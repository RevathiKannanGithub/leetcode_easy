# Leetcode problem here: https://leetcode.com/problems/two-sum/description/
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Input: nums = [2,7,11,15], target = 9
        #               0. 1. 2. 3
        l = len(nums)
        # l = 4
        for i in range(l):
            # i = 0
            r = target - nums[i]
            # r = (9 - 2) = 7
            if r in nums:
                ind = nums.index(r)
                if i!= ind:
                    return [i, ind]
