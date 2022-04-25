# https: // leetcode.com/problems/find-common-characters/


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) < 2:
            return A
        alist = set(A[0])     # make a set from first string
        res = []
        for one in alist:
            # count min frequency of every letter in every word
            n = min([a_word.count(one) for a_word in A])
            if n:    # if n>0 , we append this letter n times
                res += [one]*n
        return res
