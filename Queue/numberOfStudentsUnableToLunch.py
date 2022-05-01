#https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        
        while True:
            if sandwiches[0] not in students:
                return len(students)
            
            if sandwiches[0]==students[0]:
                #order food
                sandwiches.pop(0)
                students.pop(0)
                
            elif sandwiches[0]!=students[0]:
                students.append(students[0])
                students.pop(0)
        
            if not sandwiches and not students:
                return 0
                
        