#Problem statement - https://leetcode.com/problems/two-sum/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        sign = ''
        if x < 0:
            sign = '-'
        reverse = sign.join(str(x)[::-1])
        if str(x) == reverse:
            return True
        return False
