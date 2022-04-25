# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        print(s)
        s = s.strip()
        print(s)

        #it is trimmed
        ans = 0
        sign = None
        st = ""
        for i in range(0, len(s)):
            c = s[i:i+1]
            print(i, c)
            if i == 0:
                # we can read sign as of now
                if c == "+":
                    sign = 1
                    i = i+1
                    continue
                elif c == "-":
                    sign = -1
                    i = i+1
                    continue
                elif c.isnumeric() == False:
                    return 0
                else:
                    st = st+c
                    sign = 1
                    i = i+1
                    continue

            else:
                # we cannot read sign
                if c.isnumeric() == False:
                    break
                else:
                    st = st+c
                    i = i+1
        print(st)
        if st == "":
            return 0
        ans = sign*int(st)
        print(ans)

        if ans >= -2**31 and ans <= 2**31-1:
            return ans
        else:
            if ans < -2**31:
                return -2**31
            else:
                return 2**31-1
