#https://leetcode.com/problems/sum-of-unique-elements/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic={}
        
        for i in nums:
            if i in dic:
                dic[i]=i+1
            else:
                dic[i]=1
        
        sum=0
        for x in dic:
            if dic[x]==1:
                sum=sum+x
        return sum
        
        