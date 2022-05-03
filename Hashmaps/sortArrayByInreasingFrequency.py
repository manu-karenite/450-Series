#https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        d={}
        for x in nums:
            if x in d:
                d[x]=d[x]+1
            else:
                d[x]=1
        print(d)
        
        lis=[]
        freq={}
        for x in d:
            f=d[x]
            if f in freq:
                l=freq[f]
                l.append(x)
                l.sort(reverse=True)
                freq[f]=l
            else:
                freq[f]=[x]
        print(freq)
        
        lis=[]
        for x in freq:
            lis.append([x,freq[x]])
        print(lis)
        
        lis.sort()
        
        ans=[]
        for x in lis:
            for y in x[1]:
                temp=[y]*x[0]
                ans=ans+temp
        
        return(ans)