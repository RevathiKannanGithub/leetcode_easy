#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
#
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
#
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
#
# Example 2:
# Input: nums = [1,1]
# Output: [2]
#
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # nums = [4, 3, 2, 7, 8, 2, 3, 1]
        set_nums = set(nums)
        # set_nums = {1, 2, 3, 4, 7, 8}
        missing = []

        for i in range(1, len(nums)+1):
            # i = 1, 2, 3, 4, 5, 6, 7, 8
            if i not in set_nums:
                missing.append(i)
        # missing = [5, 6]
        return missing
