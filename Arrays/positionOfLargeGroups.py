# https:  leetcode.com/problems/positions-of-large-groups/


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        # we have 1 char atleast
        curr = [s[0:1], 0]  # [curr_char,start_index]
        ans = []
        i = 1
        while i < len(s):
            char = s[i:i+1]
            if char == curr[0]:
                # repeating, continue
                i = i+1

            else:
                # we are on the next char now
                range = i-curr[1]
                if range >= 3:
                    ans.append([curr[1], i-1])
                    curr = [s[i:i+1], i]
                else:
                    # discard
                    curr = [s[i:i+1], i]
                i = i+1

        # for the last element
        range = i-curr[1]
        if range >= 3:
            ans.append([curr[1], i-1])

        return(ans)
