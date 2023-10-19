#
# https://leetcode.com/problems/pascals-triangle/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
# Example 2:
# Input: numRows = 1
# Output: [[1]]
#
def sum_row(row: List[int]) -> List[int]:
    result = [1]
    for i in range(len(row) - 1):
        result.append(row[i] + row[i + 1])
    result.append(1)
    return result

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        previous_row = [1]
        for _ in range(numRows):
            output.append(previous_row)
            previous_row = sum_row(previous_row)
        return output
