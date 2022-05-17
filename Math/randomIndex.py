#https://leetcode.com/problems/random-pick-index/

from random import random
class Solution:

    def __init__(self, nums: List[int]):
        self.arr=nums
        d={}
        for i,x in enumerate(nums):
            if x in d:
                temp=d[x]
                temp.append(i)
                d[x]=temp
            else:
                d[x]=[i]
        self.d=d
                
        

    def pick(self, target: int) -> int:
        
        lis=self.d[target]
        x=int(random()*len(lis))
        return lis[x]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
