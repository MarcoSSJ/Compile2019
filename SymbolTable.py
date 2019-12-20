class SymbolTable:

    def __init__(self):
        self.scopes = []
        self.top = -1
        self.enterScope()

    def enterScope(self):
        """进入新的scope"""
        self.scopes.append({})
        self.top += 1

    def exitScope(self):
        """离开一个scope"""
        self.scopes.pop()
        self.top -= 1

    def addSymbol(self, symbol, val):
        """向当前scope添加新变量"""
        """如果当前scope存在就报重定义的错"""
        if self.scopes[self.top].get(symbol):
            raise Exception("symbol already defined")
        table = self.scopes[self.top]
        table[symbol] = val

    def getSymbol(self, symbol):
        """从当前scope一直向前获取symbol对应的内存"""
        for i in range(self.top, -1, -1):
            val = self.scopes[i].get(symbol)
            if val:
                return val
        return None
