class MacroList():
    """宏列表,用于进行宏替换"""
    def __init__(self):
        self.params = {} #参数表,其中键值是token名称,value是下标
        self.tokens = [] #macro后要复制的内容,其中以ITENTIFIER为分隔符

    def complicateTokenStream(self, params):
        print('complicate!!!!!!')
        for i in params:
            print(i)
        if len(params) != len(self.params):
            raise Exception('the size is not correct')#macro参数个数不匹配
        else:
            s = ''
            for token in self.tokens:
                idx = self.params.get(token)
                if idx is None:
                    s += token + ' '
                else:
                    s += params[idx] + ' ' #匹配到了相应的IDENTIFIER,进行值替换
            return s

class MacroTable():
    def __init__(self):
        self.table = {}