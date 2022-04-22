#https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        available_jewels=set()
        for x in jewels:
            available_jewels.add(x)
        count=0
        for y in stones:
            if y in available_jewels:
                count=count+1
            else:
                continue
        return count
        