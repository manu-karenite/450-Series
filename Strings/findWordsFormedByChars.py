#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d={}
        for x in chars:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        print(d)
        
        sum=0
        for z in words:
            temp={}
            for x in z:
                if x in temp:
                    temp[x]+=1
                else:
                    temp[x]=1
            print(temp)
            flag=True
            for key in temp:
                if key in d and temp[key]<=d[key]:
                    flag=True
                else:
                    flag=False
                    break
            if flag==True:
                sum=sum+len(z)
                
        return(sum)
                