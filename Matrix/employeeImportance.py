#https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
d={}
class Solution:
    
    
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees.sort(key=lambda x: x.id)
        t=0
        s=set()
        for x in employees:
            if x.id==id:
                #we have matching
                t+=x.importance
                for z in x.subordinates:
                    s.add(z)
                
                
            else:
                if x.id in s:
                    t+=x.importance
                    for z in x.subordinates:
                        s.add(z)
        return t
                
        