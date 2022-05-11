# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        least = min(nums)

        idx = nums.index(least)
        print(least, idx)

        nums = nums[idx:]+nums[0:idx]
        print(nums)

        i = 0
        j = len(nums)-1

        while i <= j:
            print(i, j)
            mid = (i+j)//2

            if nums[mid] == target:

                return (mid+idx) % len(nums)

            elif nums[mid] < target:
                i = mid+1

            elif nums[mid] > target:
                j = mid-1

        return -1
