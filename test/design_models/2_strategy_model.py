
class CashSuper:
    def AcceptCash(self,money):
        print(1)
        return 0

class CashNormal(CashSuper):
    def AcceptCash(self,money):
        print(2)
        return money

class CashRebate(CashSuper):
    discount = 0
    def __init__(self,ds):
        print(3)
        self.discount = ds
    def AcceptCash(self,money):
        print(4)
        return money * self.discount

class CashReturn(CashSuper):
    total = 0
    ret = 0
    def __init__(self,t,r):
        self.total = t
        print(5)
        self.ret = r
    def AcceptCash(self,money):
        if (money>=self.total):
            print(6)
            return money - self.ret
        else:
            print(7)
            return money

class CashContext:
    def __init__(self,csuper):
        print(8)
        self.cs = csuper
    def GetResult(self,money):
        print(9)
        return self.cs.AcceptCash(money)

if __name__ == "__main__":
    money = input("money:")
    strategy = {}
    strategy[1] = CashContext(CashNormal())
    strategy[2] = CashContext(CashRebate(0.8))
    strategy[3] = CashContext(CashReturn(300,100))
    ctype = input("type:[1]for normal,[2]for 80% discount [3]for 300 -100.")
    if ctype in strategy:
        cc = strategy[ctype]
    else:
        print "Undefine type.Use normal mode."
        cc = strategy[1]
    print "you will pay:%d" %(cc.GetResult(money))