#https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums=[int(x) for x in nums]
        nums.sort()
        nums=nums[::-1]
        return str(nums[k-1])
        