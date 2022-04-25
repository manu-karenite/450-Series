# https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        dic = {}

        i = 0
        while i < 26:
            sum = (i+97)
            dic[chr(sum)] = widths[i]
            i = i+1
        print(dic)

        line = 1
        count = 0

        j = 0
        while j < len(s):
            c = s[j:j+1]
            size = dic[c]
            temp = count+size
            if temp <= 100:
                # we can adjust
                count = count+size
                j = j+1
            else:
                # we cannot adjust
                line = line+1
                count = size
                j = j+1

        return [line, count]
