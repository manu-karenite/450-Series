#https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        
        for x in nums:
            if x%2==0:
                even.append(x)
            else:
                odd.append(x)
        print(even,odd)
        
        ans=[]
        i=0
        while i<len(nums):
            if i%2==0:
                ans.append(even[0])
                even=even[1:]
                
            else:
                ans.append(odd[0])
                odd=odd[1:]
            i=i+1
        return ans
                
        