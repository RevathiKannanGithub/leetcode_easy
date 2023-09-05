#https://leetcode.com/problems/set-mismatch/description/

#You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

#You are given an integer array nums representing the data status of this set after the error.

#Find the number that occurs twice and the number that is missing and return them in the form of an array.


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        new_i = 0
        for i in range(new_i, len(nums)-1):
            # print(‘value of i’, i)
            # print(‘value of nums[i]’, nums[i])
            # print(‘value of nums[i+1]’, nums[i+1])
            if nums[i]+1 != nums[i+1]:
                print(‘nums[i]+1 != nums[i+1]’)
                res.append(nums[i])
                res.append((nums[i+1]+1))
                # print(‘res’, res)
                new_i = i+2
                # print(‘value of new_i’, new_i)
        # print(‘value of res’, res)
        return res

  if __name__ == "__main__":
      assert Soultion().findErrorNums([1,2,2,4]) == [2,3]
      assert Soultion().findErrorNums([1,1]) == [1,1]
