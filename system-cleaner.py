#!/usr/bin/python
from os import system
delete_info="""This Script will delete the content of this folders and this files:
    - ~/Downloads/
    """
def delete_folder_content(path:str):
    system(f"rm -r {path}/*")

def main():
    print(delete_info)
    if input("Do you want to continue (y|N)").lower()=="y":
        delete_folder_content("~/Downloads")
    else:
        print("exit by user")

if __name__=="__main__":
    main()
