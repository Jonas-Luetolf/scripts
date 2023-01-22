#!/bin/python
import os
print("press ENTER to skip file")

files=list(filter(lambda f:not f.startswith('.'), os.listdir(os.getcwd())))
suffix=input("suffix for filenames: ")

for file in files:
    new_name=input(f"new name for {file}: ")

    if new_name != "":
        os.rename(file,suffix+new_name+os.path.splitext(file)[1])

print("\nnew filenames:")
print("\n".join(list(filter(lambda f:not f.startswith('.'), os.listdir(os.getcwd())))))
