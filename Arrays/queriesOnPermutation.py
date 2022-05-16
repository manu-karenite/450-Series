# https://leetcode.com/problems/queries-on-a-permutation-with-key/

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        lis = []
        for i in range(1, m+1):
            lis.append(i)
        print(lis)

        ans = []

        for x in queries:

            idx = lis.index(x)
            ans.append(idx)
            # mutate the lis
            lis = lis[0:idx]+lis[idx+1:]
            lis.insert(0, x)

        return(ans)
