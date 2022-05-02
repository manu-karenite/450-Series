#https://leetcode.com/problems/rearrange-array-elements-by-sign/submissions/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg=[]
        pos=[]
        for x in nums:
            if x<0:
                neg.append(x)
            else:
                pos.append(x)
        
        ans=[]
        
        i=0
        while i<len(nums)/2:
            ans.append(pos[i])
            ans.append(neg[i])
            i=i+1
        return ans
        