# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        i = 0
        for x in nums:
            if x in m:
                idx = fabs(i-m[x])
                if idx <= k:
                    return True

                else:
                    m[x] = i
            else:
                m[x] = i
            i = i+1

        return False
