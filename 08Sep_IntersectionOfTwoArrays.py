#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
#
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the 
# result in any order.
#
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
#
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # nums1 = [1,2,2,1]
        # nums2 = [2,2]

        res = []

        nums1_sorted = sorted(set(nums1))
        # nums1_sorted = [1, 2]
        nums2_sorted = sorted(set(nums2))
        # nums2_sorted = [2]

        for i in range(len(nums1_sorted)):
            # nums1_sorted[i] = [1, 2]
            for j in range(len(nums2_sorted)):    
                # nums2_sorted[j] = [2]
                if nums1_sorted[i] == nums2_sorted[j]:
                    # [2] = [2]
                    res.append(nums1_sorted[i])
                    # [2]

        # res = [2]
        return res
