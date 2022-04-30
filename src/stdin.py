import sys
import contextlib

class StdInHandler():

    def __init__(self):
        self.STDIN = sys.stdin

    def _set_stdin(self):
        return self.STDIN
    
    def _direct_route_stdin(self, file, inputValue):
        inputValue = inputValue.read()
        with open(file, 'w') as f:
            with contextlib.redirect_stdin(f):
                print(inputValue)

class CountLines(StdInHandler):
    def __init__(self, inputValue=None):
        self.inputValue = inputValue
        super().__init__()

    def _count_lines(self):
        if self.inputValue is not None:
            result = len(self.inputValue)
        else:
            result = len(self.STDIN.readlines())
        return result

class Unique(StdInHandler):
    def _unique(self):
        listInput = list(self.STDIN)
        tmpList = list(dict.fromkeys(listInput))
        unique = [x for i, x in enumerate(tmpList) if i == tmpList.index(x)]

        return unique