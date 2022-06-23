#https://leetcode.com/problems/rearrange-spaces-between-words/

class Solution:
    def reorderSpaces(self, text: str) -> str:
        if len(text)==0:
            return ""
        if len(text)==1:
            return text[0]
        ct=0
        for x in text:
            
            if x.isalpha()==False:
                ct+=1
        x=text.split(" ")
        x=list(filter(lambda x :x!="",x))
        if len(x)==1:
            return x[0]+" "*ct
        
        
        
        padding=ct//(len(x)-1)
        i=0
        ans=""
        for word in x:
            

            ans+=word+(" "*padding)
            
        print(ans)
        ans=ans[:len(ans)-padding]
        print(ct,padding,len(x)-1)
        remaining=ct-(padding*(len(x)-1))
        ans+=" "*remaining
        return ans
        
        