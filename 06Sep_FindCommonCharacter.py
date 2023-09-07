#
# https://leetcode.com/problems/find-common-characters/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
#
# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
#
# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
#
# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
#
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        # ["bella","label","roller"]

        if not words:
            return []

        # word[0] = "bella"
        common_chars_counter = Counter(words[0])
        # common_chars_counter = Counter({'l': 2, 'b': 1, 'e': 1, 'a': 1})

        for word in words[1:]:
            # word = "label"
            # word = "roller"

            word_counter = Counter(word)
            # word_counter = Counter({'l': 2, 'a': 1, 'b': 1, 'e': 1})
            # word_counter = Counter({'r': 2, 'l': 2, 'o': 1, 'e': 1})

            common_chars_counter = common_chars_counter & word_counter 
            # common_chars_counter = Counter({'l': 2, 'b': 1, 'e': 1, 'a': 1})
            # common_chars_counter = Counter({'l': 2, 'e': 1})

        # common_chars_counter = Counter({'l': 2, 'e': 1})
        
        common_chars = []
        for char, count in common_chars_counter.items():
            # char = 'e', count = 1
            # char = 'l', count = 2

            common_chars.extend([char] * count)
            # common_chars = ['e']
            # common_chars = ['e', 'l', 'l']
        
        # common_chars = ['e', 'l', 'l']
        return common_chars
