#https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        for x in points:
            d=((x[1]**2 + x[0]**2)**0.5)
            ans.append([d,x])
        print(ans)
        ans.sort()
        
        ans=ans[0:k]
        ans=[x[1] for x in ans]
        return ans
        