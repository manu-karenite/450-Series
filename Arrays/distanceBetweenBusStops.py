#https://leetcode.com/problems/distance-between-bus-stops/

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        small=-1
        large=-1
        if start<destination:
            small=start
            large=destination
        else:
            small=destination
            large=start
            
        
        round1=sum(distance[small:large])
        round2=sum(distance)-round1
        return min(round1,round2)
            
        