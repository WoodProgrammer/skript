from src.stdin import File, String, Unique, StdInHandler

class FileInt(File, Unique, String, StdInHandler):
    def __init__(self):
        super().__init__()

    def _tail(self, n, fileName=None):
        
        data = self.tail(n, fileName)
        self.STDIN = data

        return self

    def _cat(self, fileName):
        
        data = self.cat(fileName=fileName)
        self.STDIN = data
        return self

    def _unique(self):
        
        data = self.unique(inputValue=self.STDIN)
        return self

    def _grep(self, expression):
        
        data = self.grep("heheheh", expression)
        self.STDIN = data
        return self

    def _wc(self):
        
        data = self.count_lines(self.STDIN)
        self.STDIN = data
        return self

    def _head(self, n):
        
        data = self.head(n)
        self.STDIN = data
        return self