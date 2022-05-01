from threading import Thread, Lock
from stdin_interafce import FileInt

def hede(params):
    return params


class Script(FileInt):
    
    def __init__(self):
        self.mutex = Lock()
        super().__init__()

    def getObjs(self):
        return self.Obj

    def execution(self, function, params):

        t = Thread(target = function, args = (params,))
        t.start()

obj = Script()._tail("stdin.py", 10)._head(3)