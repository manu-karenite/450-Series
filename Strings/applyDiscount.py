#https://leetcode.com/problems/apply-discount-to-prices/

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words=sentence.split(" ")
        fin=[]
        for x in words:
            if x[0:1]!="$":
                fin.append(x)
            else:
                #means it is a dollar
                curr=x[1:]
                if curr.isnumeric()==True:
                    price=int(x[1:])
                    print(price)
                    fin1=round(((price-(discount/100)*price)),2)
                    res = "{:.2f}".format(fin1)
                    print(res)
                    fin.append("$"+str(res))
                else:
                    fin.append(x)
                    
        return " ".join(fin)
                    
                    
        