#https://leetcode.com/problems/relative-ranks/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        lis=[]
        for x in score:
            lis.append(x)
        
        lis.sort(reverse=True)
        toppers=lis[0:3]
        overs=lis[3:]
        
        d={}
        for i in range(0,len(toppers),1):
            if i==0:
                d[toppers[i]]="Gold Medal"
                
            elif i==1:
                d[toppers[i]]="Silver Medal"
            
            else:
                d[toppers[i]]="Bronze Medal"
        
        for i in range(0,len(overs),1):
            d[overs[i]]=i+1+len(toppers)
        print(d)
        ans=[]
        for x in score:
            ans.append(str(d[x]))
        return ans
            
        