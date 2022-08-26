#!/usr/bin/python
from os import listdir
from os.path import isfile
import os

def get_filetype(filename:str)->str:
    name,filetype=os.path.splitext(filename)
    return filetype
    
def get_filename(index:str,name_len:int)->str:
    zeros="0"*int(name_len-len(str(index)))
    return zeros+str(index)

def main():
    path=os.getcwd()+"/"
    original_names = [f for f in listdir(path) if isfile(path+f)]
    original_names.sort()
    name_len=len(str(len(original_names)))
    new_names=[f"{get_filename(index,name_len)}{get_filetype(name)}" for index, name in enumerate(original_names)]
    print(",".join(new_names))

    if input("This are the new filenames, do you want to continue? (y|N)") == "y":
        for original, new in zip(original_names,new_names):
            os.system(f"mv {path}{original} {path}{new}")
    else:
        print("exit by user")

if __name__=="__main__":
    main()
