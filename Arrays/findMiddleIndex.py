#https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        nums.insert(0,0)
        nums.append(0)
        print(nums)
        
        i=1
        while i<=len(nums)-2:
            
            l=nums[0:i]
            r=nums[i+1:]
            print(l,r)
            if sum(l)==sum(r):
                return i-1
            i=i+1
        return -1
        