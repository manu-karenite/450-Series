# https://leetcode.com/problems/uncommon-words-from-two-sentences/

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        a = set()
        b = set()
        # also need to check for 1 frequency

        d1 = {}
        d2 = {}
        s1 = s1.split()
        s2 = s2.split()

        for x in s1:
            if x in d1:
                d1[x] = d1[x]+1
            else:
                d1[x] = 1
        for x in s2:
            if x in d2:
                d2[x] = d2[x]+1
            else:
                d2[x] = 1

        for x in d1:
            if d1[x] == 1 and x not in d2:
                a.add(x)
        for x in d2:
            if d2[x] == 1 and x not in d1:
                b.add(x)

        u = a.union(b)
        i = a.intersection(b)

        diff = u.difference(i)
        return list(diff)
