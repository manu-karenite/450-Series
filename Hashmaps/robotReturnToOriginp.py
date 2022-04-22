#https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dire={
            "R":0,
            "L":0,
            "U":0,
            "D":0
        }
        for x in moves:
            if x not in dire:
                dire[x]=1
            else:
                dire[x]=dire[x]+1
        
        print(dire)
        return dire["R"]==dire["L"] and dire["U"]==dire["D"]
            