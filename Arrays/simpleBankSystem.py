#https://leetcode.com/problems/simple-bank-system/

class Bank:

    def __init__(self, balance: List[int]):
        self.lis=balance
        print(self.lis)
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1<=len(self.lis) and account2<=len(self.lis):
            if money<=self.lis[account1-1]:
                self.lis[account1-1]-=money
                self.lis[account2-1]+=money
                return True
        return False
       
        

    def deposit(self, account: int, money: int) -> bool:
        if account<=len(self.lis):
            self.lis[account-1]+=money
            return True
        return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if account<=len(self.lis):
            if money<=self.lis[account-1]:
                self.lis[account-1]-=money
                return True
        return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)