# https://leetcode.com/problems/perfect-number/

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        ans = []
        up = int(num**0.5)
        print(up)

        for i in range(1, up+1, 1):
            if num % i == 0:

                other = num//i
                if other != i and other != num:
                    ans.append(i)
                    ans.append(other)
                else:
                    ans.append(i)
        print(ans)
        if num in ans:
            ans.remove(num)
        ans = sum(ans)
        if ans == num:
            return True
        else:
            return False
