#https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        lis=[]
        dic={}
        for x in arr:
            count=bin(x).count("1")
            if count in dic:
                l=dic[count]
                l.append(x)
                l.sort()
                dic[count]=l
                
            else:
                dic[count]=[x]
        print(dic)
        
        for x in dic:
            lis.append([x,dic[x]])
        print(lis)
        
        lis.sort()
        ans=[]
        for x in lis:
            ans=ans+x[1]
        return(ans)
        
        