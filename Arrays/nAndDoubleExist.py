#https://leetcode.com/problems/check-if-n-and-its-double-exist/
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i,item in enumerate(arr):
            find=2*item
            if find in arr:
                
                idx=arr.index(find)
                if idx!=i:
                    return True
        return False
            
            
        