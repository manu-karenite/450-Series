# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        for i, item in enumerate(arr):
            temp = arr[i+1:]
            if len(temp) > 0:
                b = max(temp)
                ans.append(b)

            else:
                ans.append(-1)

        return(ans)
