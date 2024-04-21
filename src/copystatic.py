import os.path as path

from os import scandir, mkdir, remove
from shutil import copy, rmtree
from datetime import datetime as dt


def copy_static_to_public(src, dst):
    """
    Copies the contents of the source directory to the destination directory,
    recursively copying files and directories. If a file or directory already
    exists in the destination, it is not overwritten. The function logs each
    copied file and created directory to a file named "copy_log.txt" in the
    "logs" directory.

    Parameters:
        src (str): The path to the source directory.
        dst (str): The path to the destination directory.

    Returns:
        None
    """
    print(f"Copying static files from {src} to {dst} directory...")
    
    with open("./logs/copy_log.txt", "a") as file:
        file.write(f"\nCopying static files from {src} to {dst} started at {dt.now()}\n")
        
    items = scandir(src)
    
    for item in items:
        cur_src = path.join(src, item.name)
        cur_dst = path.join(dst, item.name)
        
        # print(f"  src: {cur_src}, dst: {cur_dst}")
        
        if item.is_file():
            if not path.exists(cur_dst) and item.name != ".DS_Store":
                copy(cur_src, cur_dst)
                
                with open("./logs/copy_log.txt", "a") as file:
                    file.write(f"   file copied from {cur_src} to {cur_dst} at {dt.now()}\n")
                    
        if item.is_dir():
            if not path.exists(cur_dst):
                mkdir(cur_dst)
                
                with open("./logs/copy_log.txt", "a") as file:
                    file.write(f"   directory created: {cur_dst} at {dt.now()}\n")
                    
                copy_static_to_public(cur_src, cur_dst)
            
    with open("./logs/copy_log.txt", "a") as file:
        file.write(f"copying from {src} to {dst} successfully finished at {dt.now()}\n")
                    
    # print("Copying successfully finished")

def delete_directory(target):
    """
    Deletes the specified target directory if it exists.

    Parameters:
        target (str): The path to the directory to be deleted.

    Returns:
        None
    """
    print(f"Deleting content of {target} directory...\n")
    
    with open("./logs/copy_log.txt", "a") as file:
        file.write(f"\n\nCleaning {target} started at {dt.now()}\n")
        
    items = scandir(target)
    
    for item in items:
        if item.is_dir():
            cur_target = path.join(target, item.name)
            rmtree(cur_target)
        else:
            remove(item)
            
    with open("./logs/copy_log.txt", "a") as file:
        file.write(f"cleaning {target} succesfully finished at {dt.now()}\n")
            
    # print("Deleting sucessfully finished")
    
    