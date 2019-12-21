class MacroList():
    def __init__(self):
        self.params = {}
        self.tokens = []

    def complicateTokenStream(self, params):
        print('complicate!!!!!!')
        for i in params:
            print(i)
        if len(params) != len(self.params):
            raise Exception('the size is not correct')
        else:
            s = ''
            for token in self.tokens:
                idx = self.params.get(token)
                if idx is None:
                    s += token
                else:
                    s += params[idx]
            return s




class MacroTable():
    def __init__(self):
        self.table = {}