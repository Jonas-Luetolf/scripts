#!/bin/python
import os

files = list(filter(lambda f: not f.startswith("."), os.listdir(os.getcwd())))
prefix = input("prefix for filenames: ")

for file in files:
    os.rename(file, prefix + file)
