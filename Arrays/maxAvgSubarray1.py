#https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #assuming k is correct
        s=sum(nums[:k])
        avg=s/k
        
        i=1
        while i<=len(nums)-k:
            s=s-nums[i-1]+nums[i+k-1]
            curr_avg=s/k
            #print(s,curr_avg,avg)
            avg=max(avg,curr_avg)
            i+=1
        return avg
        