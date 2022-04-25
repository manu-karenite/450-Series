# https://leetcode.com/problems/unique-email-addresses/submissions/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for x in emails:
            gen = x.split("@")
            local = gen[0]

            local = local.split("+")
            # get first as valid
            local = local[0]
            # remove dots
            local = local.split(".")
            local = "".join(local)

            ultimate = local+"@"+gen[1]
            print(ultimate)
            unique.add(ultimate)

        return(len(unique))
