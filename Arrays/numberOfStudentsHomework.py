#https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
        count=0
        for idx,i in enumerate(endTime):
            if i>=queryTime and startTime[idx]<=queryTime:
                count=count+1
        return count
        