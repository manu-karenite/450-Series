#https://leetcode.com/submissions/detail/685718398/

class Solution:
    def checkRecord(self, s: str) -> bool:
        count=0
        for letter in s:
            if letter=="A":
                count=count+1
        
        late=s.count("LLL")
        return count<2 and late==0
        