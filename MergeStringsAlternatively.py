#
# https://leetcode.com/problems/merge-strings-alternately/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
#
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than 
# the other, append the additional letters onto the end of the merged string. Return the merged string.
#
# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
#
# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
#
# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
#
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # word1 = "ab"
        # word2 = "pqrs"

        merged_string = ''

        for i in range(min(len(word1), len(word2))):
            merged_string += word1[i] + word2[i]
            # merged_string = a+p
            # merged_string = a+p+b+q

        return merged_string + word1[i+1:] + word2[i+1:]
        # merged_string = a+p+b+q+rs = apbqrs
