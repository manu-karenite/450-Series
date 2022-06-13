#https://leetcode.com/problems/apply-discount-every-n-orders/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n=n
        self.disc=discount
        d={}
        for i,x in enumerate(prices):
            d[products[i]]=x
            
        self.d=d
        self.curr=0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.curr+=1
        s=0
        for ids,qty in enumerate(amount):
            ids=product[ids]
            s+=qty*self.d[ids]
        if self.curr%self.n!=0:
            return s
        else:
            fi=s*((100-self.disc)/100)
            return fi
        
            
        
        
        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)