#https://leetcode.com/problems/occurrences-after-bigram/

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        l=text.split(" ")
        ans=[]
        if len(l)<3:
            return []
        
        for i in range(2,len(l),1):
            curr=l[i]
            if l[i-1]==second and l[i-2]==first:
                ans.append(curr)
                
        return ans
                
                