#https://leetcode.com/problems/find-peak-element/

class Solution:
    def getAns(self,nums:List[int],i:int,j:int) -> int :
        while i<=j:
            mid=(i+j)//2
            if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid-1
            elif nums[mid+1]>nums[mid]:
                i=mid+1
            else:
                j=mid-1
        return 0
        
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(-2**31)
        nums=nums[::-1]
        nums.append(-2**31)
        nums=nums[::-1]
        print(nums)
        i=1
        j=len(nums)-2
        
        index=self.getAns(nums,i,j)
        return index