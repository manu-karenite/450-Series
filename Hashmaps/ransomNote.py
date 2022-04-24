# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for x in magazine:
            if x in mag:
                mag[x] = mag[x]+1

            else:
                mag[x] = 1
        print(mag)

        for y in ransomNote:
            count = ransomNote.count(y)
            print(count)
            if y not in mag:
                return False

            if count > mag[y]:
                return False

        return True
