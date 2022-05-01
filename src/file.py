class File(object):
    def __init__(self, fileName):
        self.fileName = fileName

    def tail(self, n):
        content = open("{}".format(self.fileName))
        lines = content.read().splitlines()
        lines = lines[-int(n):]
        
        if n == 1:
            print(lines[n])
        elif n > 1:
            for line in lines:
                print(line)

    def head(self, n):
        content = open("{}".format(self.fileName))
        lines = content.read().splitlines()

        if n == 1:
            print(lines[n])
        elif n > 1:
            lines = lines[:int(n)]
            for line in lines:
                print(line)