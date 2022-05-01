#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        lis=[]
        
        for x in s:
            
            if x=="{" or x=="[" or x=="(":
                lis.append(x)
            else:
                if x==")":
                    if not lis:
                        return False
                    if lis[-1]!="(":
                        return False
                    lis.pop()
                    
                elif x=="}":
                    if not lis:
                        return False
                    if lis[-1]!="{":
                        return False
                    lis.pop()
                    
                elif x=="]":
                    if not lis:
                        return False
                    if lis[-1]!="[":
                        return False
                    lis.pop()
            #print(x,lis)
        if lis:
            return False
        return True
                    

        