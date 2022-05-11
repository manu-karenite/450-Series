# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i, x in enumerate(prices):
            disc = 0
            temp = prices[i+1:]
            print(temp)

            for z in temp:
                if z <= x:
                    disc = z
                    break

            ans.append(x-disc)
        return ans
