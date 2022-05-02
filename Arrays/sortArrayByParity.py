#https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        temp=[]
        for x in nums:
            if x%2==0:
                temp.append(x)
        print(temp)
        for x in nums:
            if x%2==1:
                temp.append(x)
        print(temp)
        return temp
        
        
        