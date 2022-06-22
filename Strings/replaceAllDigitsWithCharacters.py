#https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution:
    def replaceDigits(self, s: str) -> str:
        i=0
        l=len(s)
        while i<l:
            if i%2==0:
                pass
            else:
                #get the shifted char
                
                prev=s[i-1:i]
                ascii=ord(prev)
                #print(ascii)
                count=int(s[i:i+1])
                #print(count)
                replacement=chr(ascii+count)
                #print(replacement)
                s=s[:i]+replacement+s[i+1:]
            i+=1
        return(s)
            
        