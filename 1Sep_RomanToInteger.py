#
# https://leetcode.com/problems/roman-to-integer/description/?envType=daily-question&envId=2023-09-01
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
#
# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
#
# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#
# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
class Solution:
    def romanToInt(self, s: str) -> int:
        prev_value = 0
        value = 0
        total = 0
        roman = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        # s = MCMXCIV
        for char in s[::-1]:
            value = roman[char]
            #
            # char = V, value = 5
            # char = I, value = 1
            # char = C, value = 100
            # char = X, value = 10
            # char = M, value = 1000
            # char = C, value = 100
            # char = M, value = 1000
            #
            # value = 5, 5 > 0(prev_value)
            # value = 1, 1 < 5
            # value = C, 100 > 1
            # value = X, 10 < 100
            # value = M, 1000 > 10
            # value = C, 100 < 1000
            # value = M, 1000 > 100
            #
            if value < prev_value: 
                total -= value
            else:
                total += value
            # total = 5
            # total = 5 - 1 = 4
            # total = 100 + 4 = 104
            # total = 104 - 10 = 94
            # total = 1000 + 94 = 1094
            # total = 1094 - 100 = 994
            # total = 1000 + 994 = 1994
            prev_value = value
            # prev_value = 5
            # prev_value = 1
            # prev_value = 100
            # prev_value = 10
            # prev_value = 1000
            # prev_value = 100
            # prev_value = 1000
        return total
        # total = 1000 - 100 + 1000 - 10 + 100 - 1 + 5 = 1994
