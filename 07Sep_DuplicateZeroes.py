#
# https://leetcode.com/problems/duplicate-zeros/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
#
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right. Note that elements beyond the 
# length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
#
# Example 1:
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
#
# Example 2:
# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]
#
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        temp = []

        # arr = [1,0,2,3,0,4,5,0]

        while i < len(arr) - 1:
            # arr[1] = 0

            if arr[i] == 0:

                temp = arr[i:-1]
                # temp = [0, 2, 3, 0, 4, 5]

                arr[i+1] = 0
                arr[i+1:] = temp
                # arr = [1, 0, 0, 2, 3, 0, 4, 5]
                
                i = i+2
                # i = 3
            else: i += 1

        # arr = [1, 0, 0, 2, 3, 0, 0, 4]
        return arr
