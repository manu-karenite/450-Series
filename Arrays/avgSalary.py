#https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        ans=sum(salary)
        ans=ans-salary[0]-salary[-1]
        return ans/(len(salary)-2)
        