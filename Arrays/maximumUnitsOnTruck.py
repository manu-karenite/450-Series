#https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution:
    def indexone(self,arr):
        return arr[1]
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        boxTypes.sort(key=self.indexone,reverse=True)
        print(boxTypes)
        sum=0
        count=0
        for x in boxTypes:
            qty=x[0]
            unit=x[1]
            
            if count+qty<=truckSize:
                sum=sum+qty*unit
                count=count+qty
            else:
                sum=sum+(truckSize-count)*unit
                break
        
        return sum
        