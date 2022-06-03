#https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        x=address.split(".")
        x="[.]".join(x)
        return x
        