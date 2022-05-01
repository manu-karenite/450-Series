#https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        res=curr=0
        for x in s:
            if x=="(":
                curr=curr+1
                res=max(res,curr)
                
            
            elif x==")":
                curr=curr-1
        return res
        