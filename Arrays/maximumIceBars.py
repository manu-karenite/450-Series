# https://leetcode.com/problems/maximum-ice-cream-bars/
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ct=0
        costs.sort()
        for i in range(0,len(costs)):
            if coins<costs[i]:
                break
            else:
                coins-=costs[i]
                ct+=1
        return(ct)
            
            
        