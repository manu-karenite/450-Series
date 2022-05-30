#https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        ans=[]
        vow=["a","e","i","o","u","A","E","I","O","U"]
        for i,x in enumerate(s):
            cr=s[i:i+1]
            if cr in vow:
                ans.append(cr)
            
        print(ans)
        ans=ans[::-1]
        for i,x in enumerate(s):
            cr=s[i:i+1]
            if cr in vow:
                s=s[0:i]+ans[0]+s[i+1:]
                ans=ans[1:]
            
        return(s)