#https://leetcode.com/problems/k-radius-subarray-averages/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans=[-1]*len(nums)
        print(len(nums))
        if k>=len(nums):
            return ans
        #print(ans)
        si=k
        ei=len(nums)-k-1
        curr=sum(nums[si-k:si+k+1])
        avg=curr//(2*k+1)
        #here we need to manage the index out of bond
        if si<=ei:
            ans[si]=avg
            si+=1
        while si<=ei:
            #get next curr
            curr=curr-nums[si-k-1]+nums[si+k]
            avg=curr//(2*k+1)
            ans[si]=avg
            si+=1
        return(ans)