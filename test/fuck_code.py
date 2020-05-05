
import os
import shutil

def walk_test():
    filedir = "/home/hacker/Downloads/"
    for root,dirs,files in os.walk(filedir):
        for dir_list in dirs:
            print(os.path.join(root,dir_list))
        for files_list in files:
            print(os.path.join(root,files_list))
        print("##########")

walk_test()