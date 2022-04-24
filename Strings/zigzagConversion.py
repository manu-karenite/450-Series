# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, n: int) -> str:
        total = []
        for i in range(0, n):
            total.append([])

        # initialised the array

        print(total)

        direction = []
        for i in range(0, n):
            direction.append(i)

        # back
        i = n-2
        while i >= 1:
            direction.append(i)
            i = i-1
        print(direction)

        i = 0
        while i < len(s):
            letter = s[i:i+1]
            print(letter)
            idx = direction[i % len(direction)]
            # total[i%len(direction)].append(letter)
            total[idx].append(letter)
            i = i+1

        ans = ""
        for z in total:
            ans = ans+"".join(z)
        return(ans)
