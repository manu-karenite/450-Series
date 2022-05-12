#https://leetcode.com/problems/intersection-of-multiple-arrays/

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        a=set(nums[0])
        print(a)
        temp=nums[1:]
        for x in temp:
            t=set(x)
            print("t",t)
            a=a.intersection(t)
            print(a)
        
        a=list(a)
        a.sort()
        return(a)
        