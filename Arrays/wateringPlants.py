#
#https://leetcode.com/problems/watering-plants/
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        start=0
        steps=0
        cap=capacity
        i=0
        while i<len(plants):
            req=plants[i]
            
            if req<=cap:
                cap=cap-req
                #move to next
                steps+=1
                i+=1
            else:
                #donothave
                steps+=(i+1)*2-2
                #ensure it remains on curr plant
                cap=capacity
            print(steps)
        return(steps)
            
                
        