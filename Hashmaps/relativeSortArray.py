# https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        for x in arr1:
            if x in d:
                d[x] = d[x]+1
            else:
                d[x] = 1

        ans = []

        for x in arr2:
            # get freq
            f = d[x]
            lis = [x]*f
            ans = ans+lis
            d.pop(x)
        print(ans)

        temp = []
        for y in d:
            l = [y]*d[y]
            temp = temp+l
        temp.sort()
        ans = ans+temp
        return ans
