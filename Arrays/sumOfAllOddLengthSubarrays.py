#https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        i=0
        s=0
        x=len(arr)
        while i<x:
            for j in range(i+1,x+1,2):
                s+=sum(arr[i:j])
            i+=1
        return s
                
                
        