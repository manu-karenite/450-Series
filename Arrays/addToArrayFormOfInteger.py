#https://leetcode.com/problems/add-to-array-form-of-integer/
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        lis=[str(x) for x in num]
        x="".join(lis)
        ans=int(x)+k
        lis=[]
        ans=str(ans)
        for x in ans:
            lis.append(int(x))
            
        print(lis)
        return lis