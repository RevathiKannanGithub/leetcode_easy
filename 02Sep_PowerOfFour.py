#
# https://leetcode.com/problems/power-of-four/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
#
# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4x.
#
# Example 1:
# Input: n = 16
# Output: true
#
# Example 2:
# Input: n = 5
# Output: false
#
# Example 3:
# Input: n = 1
# Output: true
#
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # n = 16
        if n <= 0:
            return False
        if n == 1:
            return True
        while n != 1:
            # n%4 = 0 -> 16%4 = 0
            # n%4 = 0 -> 4%4 = 0
            if n % 4 != 0:
                return False
            n = n // 4
            # n = 16//4 = 4
            # n = 4//4 = 1
        return True
