#
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
#
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
# Example 2:
# Input: s = "God Ding"
# Output: "doG gniD"
#
class Solution:
    def reverseWords(self, s: str) -> str:
        # s = "Let's take LeetCode contest"
        res = ''
        words_list = s.split()
        # words_list ["Let's", 'take', 'LeetCode', 'contest']
        for i in range(len(words_list)):
            words_list[i] = words_list[i][::-1]
        res = ' '.join(words_list)
        # s'teL ekat edoCteeL tsetnoc
        return res
