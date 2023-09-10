#
# https://leetcode.com/problems/palindromic-substrings/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
#
class Solution:
    def countSubstrings(self, s: str) -> int:
        # s = "abc"
        # s = "aaa"
        result = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                # a, b, c
                # a, a, a, aa, aa, aaa
                if s[i:j+1] == s[i:j+1][::-1]:
                    result += 1
        return result
