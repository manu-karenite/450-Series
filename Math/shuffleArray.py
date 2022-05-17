#https://leetcode.com/problems/shuffle-an-array/

from random import shuffle
class Solution:

    def __init__(self, nums: List[int]):
        self.lis=nums
        

    def reset(self) -> List[int]:
        return self.lis
        

    def shuffle(self) -> List[int]:
        temp=[]
        for x in self.lis:
            temp.append(x)
        shuffle(temp)
        return temp
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
