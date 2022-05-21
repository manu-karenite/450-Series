#https://leetcode.com/problems/xor-operation-in-an-array/
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans=[]
        for i in range(1,n+1,1):
            ans.append(start+2*(i-1))
        l=ans[0]
        ans=ans[1:]
        for x in ans:
            l=l^x
        return l