#https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=[0]
        for i,item in enumerate(gain):
            ans.append(ans[-1]+item)
        print(ans)
        ans.sort()
        return ans[-1]
            
        