#https://leetcode.com/problems/sort-characters-by-frequency/
class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for x in s:
            if x in d:
                d[x]=d[x]+1
            else:
                d[x]=1
        
        #ok
        ans=[]
        for y in d:
            ans.append([d[y],y])
        
        print(ans)
        ans.sort(reverse=True)
        
        ret=""
        for x in ans:
            ret=ret+x[1]*x[0]
        return(ret)
        