# https://leetcode.com/problems/two-out-of-three/

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        a = set()
        b = set()
        c = set()

        for x in nums1:
            a.add(x)
        for y in nums2:
            b.add(y)

        for z in nums3:
            c.add(z)

        temp1 = a.intersection(b)
        temp2 = b.intersection(c)
        temp3 = c.intersection(a)

        ans = temp1.union(temp2)
        ans = ans.union(temp3)
        return list(ans)
