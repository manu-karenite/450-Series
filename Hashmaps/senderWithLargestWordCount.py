#https://leetcode.com/problems/sender-with-largest-word-count/

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        
        d={}
        for i,x in enumerate(messages):
            l=x.split(" ")
            if senders[i] in d:
                d[senders[i]]+=len(l)
            else:
                d[senders[i]]=len(l)
        #print(d)
        maxi=-2**31
        fin=[]
        for x in d:
            maxi=max(d[x],maxi)
            fin.append([x,d[x]])
        
        #print(maxi)
        #print(fin)
        m=""
        for z in fin:
            if z[1]==maxi:
                if z[0]>m:
                    m=z[0]
        return(m)
            
            
            
                
        