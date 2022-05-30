#https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d={}
        for x in arr:
            if x in d:
                d[x]+=1
            else:
                d[x]=1

        lis=[]
        for x in d:
            lis.append([d[x],x])
        lis.sort(reverse=True)
        print(lis)
        
        size=len(arr)
        s=set()
        count=0
        for x in lis:
            count+=x[0]
            s.add(x[1])
            if count>=(size//2):
                break
        return(len(s))
        