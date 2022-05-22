#https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution:
    def checkString(self, s: str) -> bool:
        lis=[]
        orig=[]
        for x in s:
            lis.append(x)
            orig.append(x)
        print(lis)
        
        lis.sort()
        
        return lis==orig
        