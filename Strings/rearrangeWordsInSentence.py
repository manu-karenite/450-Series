#https://leetcode.com/problems/rearrange-words-in-a-sentence/

class Solution:
    def arrangeWords(self, text: str) -> str:
        d={}
        s=text.split(" ")
        for x in s:
            z=len(x)
            if z in d:
                temp=d[z]
                temp.append(x)
                d[z]=temp
            else:
                d[z]=[x]
        print(d)
        lis=[]
        for x in d:
            sent=" ".join(d[x])
            lis.append([x,sent])
        
        lis.sort(key=lambda x :  x[0])
        print(lis)
        
        lis=[x[1] for x in lis]
        print(lis)
        lis=" ".join(lis).lower()
        lis=lis[0:1].upper()+lis[1:]
        return lis