#
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
#
# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
#
# Example 1:
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
#
# Example 2:
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
#
# Example 3:
# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"
# Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
#
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        dict_letters = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
            'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16,
            'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
            'y': 25, 'z': 26
            }
        # letters = ['c', 'f', 'j']
        first_char_flag = 0

        for char in letters:
            # char = c, f, j
            # target = a
            if first_char_flag == 0:
                first_char_letter = char
                first_char_flag = 1

                # dict_letters[char] = 3
                # dict_letters[char] = 6
                # dict_letters[char] = 10

            least_diff = dict_letters[char] - dict_letters[target]
            # least_diff = 3 - 1 = 2

            if least_diff > 0:
                return char
                
        return first_char_letter
