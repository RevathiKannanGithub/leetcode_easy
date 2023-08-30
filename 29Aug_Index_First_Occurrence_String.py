# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #haystack = leetcode
        #needle = leeto
        for i in range(0, len(haystack)):
            #value of i: 0, 1, 2, 3, 4, 5, 6
            #substring: l, le, lee, leet, leetc, leetco, leetcod, leetcode
            for j in range(i, len(haystack)):
            # substring:1 - le, lee, leet, leetc, leetco, leetcod, leetcode
            # substring:2 - e, ee, eet, eetc, eetco, eetcod, eetcode
            # substring:3 - e, et, etc, etco, etcod, etcode
            # substring:4 - t, tc, tco, tcod, tcode
            # substring:5 - c, co, cod, code
            # substring:6 - o, od, ode
            # substring:7 - d, de
            # substring:8 - e
                if(haystack[i:j+1] == needle):
                    return (i)
        return -1
