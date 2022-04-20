#https://leetcode.com/problems/move-zeroes/submissions/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        originalLeng=len(nums)
        leng = len(nums)
        i=0
        count=0
        while i<leng:
            if nums[i]==0:
                nums.remove(0)
                leng=len(nums)
                count=count+1
            else:
                i=i+1
        i=0
        target=originalLeng-leng
        
        while i<target:
            nums.append(0)
            i=i+1
        