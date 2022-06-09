#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        for x in nums:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        print(d)
        
        i=0
        s=0
        for x in d:
            freq=min(d[x],2)
            s+=freq
            print(i,i+freq)

            z=i+freq
            while i<z:
                nums[i]=x
                i+=1
            
            
        
        print(nums)
        return (s)
        