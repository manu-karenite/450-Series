#https://leetcode.com/problems/print-words-vertically/

class Solution:
    def printVertically(self, s: str) -> List[str]:


        words=s.split(" ")
        fin=s.split(" ")
        fin.sort(key=lambda x: len(x))
        rows=len(fin[-1])
        cols=len(fin)
        print(rows,cols)
        for i in range(0,len(words),1):
            z=len(words)
            st=words[i]+" "*(rows-len(words[i]))
            print(st,len(st))
            words[i]=st
        print(words)
            
        ans=[]
        
        
        for r in range(0,rows,1):
            s=""
            for c in range(0,cols,1):
                c=words[c][r:r+1]

                s+=c
            
            x=s.rstrip()
            ans.append(x)
        #print(ans)
        return ans
                
        
            
        
        
        