#!/usr/bin/python
from os import system
delete_info="""This Script will delete the content of this folders and this files:
    - ~/Downloads/
    """

folders_to_clear=["~/Downloads"]

def clear_folders(to_clear):
    for i in to_clear:
        delete_folder_content(i)

def delete_folder_content(path:str):
    system(f"rm -r {path}/*")

def main():
    print(delete_info)
    if input("Do you want to continue (y|N)").lower()=="y":
        for folder in folders_to_clear: 
            delete_folder_content(folder)
    else:
        print("exit by user")

if __name__=="__main__":
    main()
