#Copyright (c) 2022 Jonas Lütolf
#!/usr/bin/python
from os import listdir,getcwd,system
from os.path import isfile,splitext
from sys import argv

def get_filetype(filename:str)->str:
    name,filetype=splitext(filename)
    return filetype
    
def get_filenumber(index:str,name_len:int)->str:
    zeros="0"*int(name_len-len(str(index)))
    return zeros+str(index)

def gen_filenames(original_names:list,hold_name:bool):
    new_names=[]
    name_len=len(str(len(original_names)))
    for index,name in enumerate(original_names):
        if hold_name:
            new_names.append(f"{get_filenumber(index,name_len)}_{name}")
        else:
            new_names.append(f"{get_filenumber(index,name_len)}{get_filetype(name)}")

    return new_names

def main():
    path=getcwd()+"/"
    original_names = [f for f in listdir(path) if isfile(path+f)]
    original_names.sort()       
        
    new_names=gen_filenames(original_names,"-a" in argv)
    print(",".join(new_names))

    if input("This are the new filenames, do you want to continue? (y|N)").lower() == "y":
        for original, new in zip(original_names,new_names):
            system(f"mv '{path}{original}' '{path}{new}'")
    else:
        print("exit by user")

if __name__=="__main__":
    main()
