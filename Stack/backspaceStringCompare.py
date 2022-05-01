#https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def getAns(self,s:str) -> str:
        i=0
        lis=[]
        while i<len(s):
            x=s[i:i+1]
            
            if x!="#":
                lis.append(x)
            else:
                #when a backspace char is there
                lis.append(x)
                #now start popping:
                lis.pop()
                #remove the char lso
                if len(lis)>0:
                    lis.pop()
            i=i+1
        return "".join(lis)
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        
        lef=self.getAns(s)
        rig=self.getAns(t)
        print(lef,rig)
        if lef!=rig:
            return False
        else:
            return True
        