#
# https://leetcode.com/problems/backspace-string-compare/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
#
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.
#
# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
#
# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
#
# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
#
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_backspaced = []
        t_backspaced = []
        
        # s = 'ab#c'
        # t = 'ad#c'

        for i in range(0, len(s)):
            # s[i] = 'a'
            # s[i] = 'b'
            # s[i] = '#'
            # s[i] = 'c'
            # s_backspaced = ['a', 'b']
            # s[i] = '#', s_backspaced = ['a', 'c']

            if s[i] == '#':
                if s_backspaced: 
                    s_backspaced.pop()
            else:
                s_backspaced.append(s[i])

        for j in range(0, len(t)):
            # t[j] = 'a'
            # t[j] = 'd'
            # t[j] = '#'
            # t[i] = 'c'
            # t_backspaced = ['a', 'd']
            # t[j] = '#', t_backspaced = ['a', 'c']

            if t[j] == '#':
                if t_backspaced:
                    t_backspaced.pop()
            else:
                t_backspaced.append(t[j])

        # s_backspaced = ['a', 'c'] = t_backspaced = True

        return s_backspaced == t_backspaced
