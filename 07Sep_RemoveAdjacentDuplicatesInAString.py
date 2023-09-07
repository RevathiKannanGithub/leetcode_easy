#
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
#
# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.
# We repeatedly make duplicate removals on s until we no longer can. Return the final string after all such duplicate removals have been made. It can be proven 
# that the answer is unique.
#
# Example 1:
# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  
# The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
#
# Example 2:
# Input: s = "azxxzy"
# Output: "ay"
#
class Solution:
    def removeDuplicates(self, s: str) -> str:

        # s = "abbaca"

        i = 0
        s = list(s)

        # s = ['a', 'b', 'b', 'a', 'c', 'a']

        while i < len(s) - 1:

            # i = 0
            # s[i] = 'a'
            # s[i+1] = 'b'
            # i = i+1 = 0+1 = 1
            # ['a', 'b', 'b', 'a', 'c', 'a']

            # i = 1
            # s[i] = 'b'
            # s[i+1] = 'b'
            # s[i] == s[i+1]
            # i = i-1 = 1-1 = 0
            # ['a', 'a', 'c', 'a']

            # i = 0
            # s[i] = 'a'
            # s[i+1] = 'a'
            # s[i] == s[i+1]
            # ['c', 'a']

            if s[i] == s[i + 1]:
                del s[i]
                del s[i]
                if i: i -= 1
            else: i += 1

        # s = "ca"
        return ''.join(s)
