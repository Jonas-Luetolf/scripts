#!/usr/bin/python
from os import listdir
from os.path import isfile
import os

def get_filetype(filename:str):
    filename="".join(list(reversed(filename)))
    return ("".join(list(reversed(filename[0:filename.find(".")+1])))).lower()
    
def get_filename(index,name_len):
    zeros="0"*int(name_len-len(str(index)))
    return zeros+str(index)

path=os.getcwd()+"/"
files = [f for f in listdir(path) if isfile(path+f)]
files.sort()

name_len=len(str(len(files)))
new_names=[f"{get_filename(index,name_len)}{get_filetype(name)}" for index, name in enumerate(files)]

print(",".join(new_names))

if input("This are the new filenames, do you want to continue? (y|N)") == "y":
    for original, new in zip(files,new_names):
        os.system(f"mv {path}{original} {path}{new}")
