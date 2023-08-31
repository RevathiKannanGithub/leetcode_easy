# https://leetcode.com/problems/majority-element/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
#
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      # nums = [3, 2, 3]
      a = Counter(nums)
      # a = Counter({3: 2, 2: 1})
      max_value = 0
      result = 0
      for i, j in a.items():
        # i = 3, j = 2
        # i = 2, j = 1
        if j > max_value:
          result = i
          max_value = j
          # result = 3
          # max_value = 2
      return result
