# skript
Skript is wrapper of the shell command to use them in Python3.x.This wrapper allows system administrations easily develop shell scripts the person who familiar with Python3.x

Inspired from ; https://github.com/bitfield/script

With this simple wrapper you are able to develop python scripts to use them in python.

## Example Usage

```py
from src.stdin import *
from src.stdin_interface import *
from src.process import Script

Script()._cat("file.txt")._tail(8)._head(4)
```

Supported UNIX/Shell command allows you to use pipe the outputs between functions.

| Unix/Shell  | skript  |
| :---        |    :----:   |
| cat      | _cat  :white_check_mark:     |
| tail   | _tail   :white_check_mark:     |
| head   | _head  :white_check_mark: | 
| wc -l   | _unique  :warning: | 
| unique   | _unique  :warning: | 
| exec   | _exec  TODO | 
| find   | find  TODO |
| grep   | _exec  TODO |
| kubectl -o jsonpath  | _kubectl  TODO |