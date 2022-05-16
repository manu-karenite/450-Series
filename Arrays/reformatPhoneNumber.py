# https://leetcode.com/problems/reformat-phone-number/

class Solution:
    def reformatNumber(self, number: str) -> str:
        lis = []
        for x in number:
            if x.isdigit() == True:
                lis.append(x)
        print(lis)

        i = 0
        ans = []
        while len(lis) > 4:
            temp = lis[0:3]
            curr = "".join(temp)
            ans.append(curr)
            lis = lis[3:]
        if len(lis) <= 3:
            ans.append("".join(lis))
        elif len(lis) == 4:
            ans.append("".join(lis[0:2]))
            ans.append("".join(lis[2:]))

        return "-".join(ans)
