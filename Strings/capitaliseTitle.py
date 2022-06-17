#https://leetcode.com/problems/capitalize-the-title/

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s=""
        l=title.split(" ")
        for i,x in enumerate(l):
            if len(x)<=2:
                s=x.lower()
                l[i]=s
                
            else:
                s=x[0:1].upper()+x[1:].lower()
                l[i]=s
        print(l)
        return " ".join(l)
                
        