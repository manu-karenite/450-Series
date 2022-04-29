#https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for x in nums:
            if x in d:
                d[x]=d[x]+1
            else:
                d[x]=1
        
        print(d)
        ans=[]
        for y in d:
            ans.append([d[y],y])
        print(ans)
        
        ans.sort(reverse=True)
        #on the frequency
        ans=ans[0:k]
        print(ans)
        ans=[x[1] for x in ans]
        return ans