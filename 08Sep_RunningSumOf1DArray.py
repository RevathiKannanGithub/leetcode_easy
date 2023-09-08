#
# https://leetcode.com/problems/running-sum-of-1d-array/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
#
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.
#
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
#
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
#
# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
#
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        res = []
        total = 0

        # nums = [1,2,3,4]

        for i in range(len(nums)):
            # nums[i] = 1, 2, 3, 4

            total += nums[i]

            # total = 1
            # total = 1+2 = 3
            # total = 1+2+3 = 6
            # total = 1+2+3+4 = 10

            res.append(total)

            # res = [1]
            # res = [1, 3]
            # res = [1, 3, 6]
            # res = [1, 3, 6, 10]
        
        # res = [1, 3, 6, 10]

        return res
