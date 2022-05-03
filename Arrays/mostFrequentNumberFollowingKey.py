#https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        i=0
        d={}
        while i<len(nums)-1:
            if nums[i]==key:
                #get the next one
                nex=nums[i+1]
                
                if nex in d:
                    d[nex]=d[nex]+1
                else:
                    d[nex]=1
                    
            
            
            
            i=i+1
        print(d)
        return max(d,key=lambda x : d[x])