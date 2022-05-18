# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp = [0]*len(nums)

        for i, item in enumerate(nums):
            temp[item-1] = temp[item-1]+1
        print(temp)
        lis = []
        for i, x in enumerate(temp):
            if x == 0:
                lis.append(i+1)
        return lis
