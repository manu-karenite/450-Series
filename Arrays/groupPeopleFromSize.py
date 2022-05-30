#https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d={}
        for i,x in enumerate(groupSizes):
            if x in d:
                lis=d[x]
                lis.append(i)
                d[x]=lis
            else:
                d[x]=[i]
        print(d)
        
        ans=[]
        for z in d:
            size=z
            members=d[z]
            start=0
            while start<len(members):
                temp=members[start:start+size]
                ans.append(temp)
                start+=size
            
        return(ans)
        
        