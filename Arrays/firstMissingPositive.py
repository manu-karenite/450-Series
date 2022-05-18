# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        a = set(nums)
        nums = list(a)
        print(nums)
        nums.sort()
        if nums[0] > 0 or nums[0] < 0:

            count = 1
            for x in nums:
                if x != count and x > 0:
                    return count
                if x > 0:
                    count = count+1
            return count
        elif nums[0] == 0:
            count = 0
            for x in nums:
                if x != count:
                    return count

                count = count+1

            return count
