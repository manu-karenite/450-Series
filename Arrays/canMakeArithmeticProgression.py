#https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        s=set()
        
        for i  in range(0,len(arr)-1):
            s.add(arr[i+1]-arr[i])
        
        if len(s)==1:
            return True
        else:
            return False
            
            
        