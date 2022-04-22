#https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        #fisrt check whether the characters are same present or not
        
        letters={}
        
        for x in s:
            if x not in letters:
                letters[x]=1
            else:
                letters[x]=letters[x]+1

        
        #start removing the letters on match
        
        for x in goal:
            if x not in letters:
                return False
            else:
                if letters[x]==1:
                    letters.pop(x)
                else:
                    letters[x]=letters[x]-1
        
        #get the length of any word
        leng=len(s)
        #s is the original word
        for i in range(1,leng+1):
            s=s[-1]+s[0:leng-1]
            print(s)
            if s==goal:
                return True
            else:
                continue
        return False
            
            
        
        