#
# https://leetcode.com/problems/counting-bits/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
#
# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
#
# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#
class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            binary = bin(i).replace("0b", "")
            j = count = 0
            while j < len(binary):
                if binary[j] == '1':
                    count += 1
                j += 1
            output.append(count)
        return output
