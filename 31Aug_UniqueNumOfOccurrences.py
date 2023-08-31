# https://leetcode.com/problems/unique-number-of-occurrences/
#
#######################
# PROBLEM DESCRIPTION #
#######################
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
#
# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
#
# Example 2:
# Input: arr = [1,2]
# Output: false
#
# Example 3:
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
#
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # arr = [1,2,2,1,1,3]
        a = Counter(arr)
        # a = Counter({1: 3, 2: 2, 3: 1})
        occurrence = set()
        for i, j in a.items():
            # i = 1, j = 3
            # i = 2, j = 2
            # i = 3, j = 1
            if j in occurrence:
                return False
            occurrence.add(j)
        return True
# final result = True
