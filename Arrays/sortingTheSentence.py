#https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def byFirst(self,lis):
        return lis[0]
    def sortSentence(self, s: str) -> str:
        s=s.split(" ")
        ans=[]
        for x in s:
            l=int(x[-1])
            ans.append([l,x[:len(x)-1]])
        
        ans.sort(key=self.byFirst)
        print(ans)
        st=""
        for x in ans:
            st=st+x[1]+" "
        return(st[:len(st)-1])

            