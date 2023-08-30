# https://leetcode.com/problems/palindrome-number/
#
#######################
# PROBLEM DESCRIPTION #
#######################
# Given an integer x, return true if x is a 
# palindrome, and false otherwise.
#
# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#    
# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#    
# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #x = 121
        sign = ''
        if x < 0:
            sign = '-'
        reverse = sign.join(str(x)[::-1])
        #reverse = 121
        if str(x) == reverse:
            return True
        return False
        #Result = True
