#https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

class Solution:
    
    def case1(self,s):
        #cannot contain spaces
        for x in s:
            if x.isnumeric()==True:
                return False
        return True
        
        
        
    def case2 (self,s):
        hyphen_indices=[]
        i=0
        for x in s:
            if x=="-":
                hyphen_indices.append(i)
            i+=1
        l=len(hyphen_indices)
        if l>1:
            return False
        if l==0:
            return True
        #when we have l
        idx=hyphen_indices[0]
        if idx==0 or idx==l-1:
            return False
        #now in middle
        prev=s[idx-1:idx]
        
        nex=s[idx+1:idx+2]
        #print(prev,nex)
        if prev.isalpha()==True and nex.isalpha()==True:
            return True
        else:
            return False
                
        
    def case3(self,s):
        p=["!",".",","]
        punct_indices=[]
        i=0
        for x in s:
            if x in p:
                punct_indices.append(i)
            i+=1
        l=len(punct_indices)
        if l>1:
            return False
        if l==0:
            return True
        #when we have l
        idx=punct_indices[0]
        #print(idx,punct_indices,s,l)
        if idx!=len(s)-1:
            return False
        return True
    
    def countValidWords(self, sentence: str) -> int:
        s=sentence.split(" ")
        s=list(filter(lambda x: x!="",s))
        #print(s)
        ct=0
        for x in s:
            a=self.case1(x)
            
            b=self.case2(x)
            
            c=self.case3(x)
            
            if a and b and c:
                ct+=1
                #print(x)
        return ct
        