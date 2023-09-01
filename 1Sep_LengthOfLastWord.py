#
# https://leetcode.com/problems/length-of-last-word/submissions/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
#
# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#  
# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#  
# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s = "Hello World"
        length = 0
        words_list = []
        words_list = s.split()
        # words_list = ['Hello', 'World']
        for i in range(len(words_list)):
            last_word = words_list[i]
            # last_word = "Hello"
            # last_word = "World"
        length = len(last_word)
        # length = 5
        return length
