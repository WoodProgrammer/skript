from stdin import File, Unique, StdInHandler

class FileInt(File, Unique, StdInHandler):
    def __init__(self):
        super().__init__()

    def _tail(self, arg1, arg2):
        
        data = self.tail(arg1, arg2)
        self.STDIN = data

        return self

    def _head(self, n):
        
        data = self.head(n)
        self.STDIN = data
        return self