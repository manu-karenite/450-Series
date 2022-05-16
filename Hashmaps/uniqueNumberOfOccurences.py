# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for x in arr:
            if x in dic:
                dic[x] = dic[x]+1
            else:
                dic[x] = 1

        print(dic)

        f = set()

        for key in dic:
            value = dic[key]
            if value in f:
                return False
            f.add(value)

        return True
