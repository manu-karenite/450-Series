# https://leetcode.com/problems/count-sorted-vowel-strings/
class Solution:

    def returnTemp(self, n):
        a = ['a', 'e', 'i', 'o', 'u']
        e = ['e', 'i', 'o', 'u']
        i = ['i', 'o', 'u']
        o = ['o', 'u']
        u = ['u']

        if n == 1:
            return [['a', 'e', 'i', 'o', 'u'], 5]

        # otherwise

        # get from n-1 first
        ans = self.returnTemp(n-1)

        temp = []
        count = 0

        for x in ans[0]:
            # get the last character
            c = x[-1]

            if c == 'a':
                for y in a:
                    temp.append(x+y)
                    count = count+1

            elif c == 'e':
                for y in e:
                    temp.append(x+y)
                    count = count+1

            elif c == 'i':
                for y in i:
                    temp.append(x+y)
                    count = count+1

            elif c == 'o':
                for y in o:
                    temp.append(x+y)
                    count = count+1

            elif c == 'u':
                for y in u:
                    temp.append(x+y)
                    count = count+1

        return [temp, count]

    def countVowelStrings(self, n: int) -> int:

        ans = self.returnTemp(n)
        return ans[1]
