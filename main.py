from src.stdin import *
from src.stdin_interface import *
from src.process import Script

Script()._cat("README.md")
Script()._cat("README.md")._wc()
Script()._cat("file.txt")._tail(8)._head(4)