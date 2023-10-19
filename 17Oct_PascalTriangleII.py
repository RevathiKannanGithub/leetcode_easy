#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
#####################################################################################################################################################
#
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
#
# Example 2:
# Input: rowIndex = 0
# Output: [1]
#
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
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

    def getRow(self, rowIndex: int) -> List[int]:
        result = self.generate(rowIndex + 1)[-1]
        return result
