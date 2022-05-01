import sys
import numpy as np
import contextlib


class StdInHandler():

    def __init__(self):
        self.STDIN = None

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

    def __init__(self):
        super().__init__()

    def unique(self, inputValue=None):
        tmpList = []
        if inputValue is not None:
            listInput = inputValue
        else:
            listInput = self.STDIN

        for data in listInput:
            tmpList.append(data)

        unique = np.unique(np.array(tmpList))

        return unique

class File(object):
    def __init__(self):
        pass

    def tail(self, fileName, n):
        content = open("{}".format(fileName))
        lines = content.read().splitlines()
        
        
        if n == 1:
            print(lines[n])
        elif n > 1:
            lines = lines[-int(n):]
            for line in lines:
                print(line)
        
        return lines

    def head(self, fileName, n):
        content = open("{}".format(fileName))
        lines = content.read().splitlines()

        if n == 1:
            print(lines[n])
        elif n > 1:
            lines = lines[:int(n)]
            for line in lines:
                print(line)