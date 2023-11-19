#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
# 
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
#
# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true
#
# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true
#
# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
#
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k==0:return False
        set_=set()
        for r in range(len(nums)):
            if nums[r] in set_:return True
            set_.add(nums[r])
            if len(set_)==k+1:set_.remove(nums[r-k])
        return False
