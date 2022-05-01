import re
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

class String(StdInHandler):
    def __init__(self):
        super().__init__()
    
    def grep(self, inputValue=None, inputExpression=None):
        pattern = re.compile(inputExpression)
        pattern.search(str(inputValue))
        print(pattern)
        return pattern

class Unique(StdInHandler):

    def __init__(self):
        super().__init__()

    def unique(self, inputValue=None):
        tmpList = []
        listInput = inputValue
        

        for data in listInput:
            tmpList.append(data)

        unique = np.unique(np.array(tmpList))

        return unique

class File(object):
    def __init__(self):
        pass


    def count_lines(self, inputValue=None):
        result = len(inputValue)
        print(result)
        return result
        
    def cat(self, fileName):
        content = open("{}".format(fileName))
        lines = content.read().splitlines()
        content.close()

        return lines

    def tail(self, n, fileName=None):
        output_list = []

        if fileName is not None:
            content = open("{}".format(fileName))
            
            lines = content.read().splitlines()
        else:
            lines = self.STDIN

        if n == 1:
            print(lines[n])
            output_list.append(lines[n])
        elif n > 1:
            lines = lines[-int(n):]
            for line in lines:
                output_list.append(line)
        
        print(output_list)

        return output_list

    def head(self, n):

        content = self.STDIN

        lines = list(content)
        if n == 1:
            print(lines[n])
        elif n > 1:
            lines = lines[:int(n)]
            for line in lines:
                print(line)

        return lines