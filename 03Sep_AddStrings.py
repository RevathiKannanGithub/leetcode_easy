#
# https://leetcode.com/problems/add-strings/description/
#
#####################################################################################################################################################
#                                                            PROBLEM DESCRIPTION                                                                    #
######################################################################################################################################################
#
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
#
# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"
#
# Example 2:
# Input: num1 = "456", num2 = "77"
# Output: "533"
#
# Example 3:
# Input: num1 = "0", num2 = "0"
# Output: "0"
#
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        # num1 = "11", num2 = "123"
        
        def str2int(num):
            output = 0
            numDict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,
                       '6':6, '7':7, '8':8, '9':9}
            # num = "11"
            # num = "123"
            for d in num:
                # num = '11'
                # d = '1'
                # d = '1'
                # num = '123
                # d = '1'
                # d = '2'
                # d = '3'
                output = output*10 + numDict[d]
                # num = '11'
                # output = 0*10 + 1 = 1
                # output = 1*10 + 1 = 11
                # num = '123'
                # output = 0*10 + 1 = 1
                # output = 1*10 + 2 = 12
                # output = 12*10 + 3 = 123
            return output
          
# Below line of code is added on facing "ValueError: Exceeds the limit (4300) for integer string conversion" for the input
# num1 = “1”, num2 = “9999999999999999999999999999999999999999999999999999999999999999999999999999..."
      
        sys.set_int_max_str_digits(10000)
        
        return str(str2int(num1) + str2int(num2))
        # 11 + 123 = 134
