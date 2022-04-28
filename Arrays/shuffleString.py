#https://leetcode.com/problems/shuffle-string/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=['a']*len(s)
        print(ans)
        for i,item in enumerate (indices):
            ans[item]=s[i:i+1]
        ans="".join(ans)
        return ans