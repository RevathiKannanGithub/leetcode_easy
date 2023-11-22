#
# https://leetcode.com/problems/is-subsequence/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise. A subsequence of a string is a new string that is formed from 
# the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
#
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left_limit = len(s)
        right_limit = len(t)

        p_left = p_right = 0
        while p_left < left_limit and p_right < right_limit:
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1
        
        return p_left == left_limit
