#
# https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
# 
# Given an integer array nums, return 0 if the sum of the digits of the minimum integer in nums is odd, or 1 otherwise.
#
# Example 1:
# Input: nums = [34,23,1,24,75,33,54,8]
# Output: 0
# Explanation: The minimal element is 1, and the sum of those digits is 1 which is odd, so the answer is 0.
#
# Example 2:
# Input: nums = [99,77,33,66,55]
# Output: 1
# Explanation: The minimal element is 33, and the sum of those digits is 3 + 3 = 6 which is even, so the answer is 1.
#
class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:

        res = 0
        
        # nums = [99,77,33,66,55]
        nums.sort()
        # nums = [33, 55, 66, 77, 99]

        min_nums = nums[0]
        # min_nums = 33

        min_nums = [int(digit) for digit in str(min_nums)]
        # min_nums [3, 3]

        for i in range(len(min_nums)):
            res += min_nums[i]

        # res = 3 + 3 = 6

        if res%2 == 0:
            return 1
        else:
            return 0

        # return 0
