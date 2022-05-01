#https://leetcode.com/problems/baseball-game/


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        ans=[]
        for i,x in enumerate(ops):
            if x=="+":
                l=ans[-1]
                r=ans[-2]
                ans.append(l+r)
                
            elif x=="D":
                l=ans[-1]
                ans.append(2*l)
            
            elif x=="C":
                ans.pop()
                
            else:
                ans.append(int(x))
        print(ans)
        
        return sum(ans)