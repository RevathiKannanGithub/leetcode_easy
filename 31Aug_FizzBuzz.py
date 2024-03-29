# https://leetcode.com/problems/fizz-buzz/description/
#
#######################
# PROBLEM DESCRIPTION #
#######################
# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
#
# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]
#
# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
#
# Example 3:
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
#
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # n = 3
        result = []
        for i in range(1, n+1):
            # i = 1, 2, 3
            if (i % 3 == 0) and (i % 5 == 0):
                result.append("FizzBuzz")           
            elif i % 3 == 0:
                # i = 3, "Fizz"
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                # i = 1, "1"
                # i = 2, "2"
                result.append(str(i))
        return result
# result = ['1', '2', "Fizz"]
