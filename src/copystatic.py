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
    items = scandir(src)
    for item in items:
        cur_src = path.join(src, item.name)
        cur_dst = path.join(dst, item.name)
        print(f"src: {cur_src}, dst: {cur_dst}")
        if item.is_file():
            if not path.exists(cur_dst):
                copy(cur_src, cur_dst)
                with open("./logs/copy_log.txt", "a") as file:
                    file.write(f"file copied from {cur_src} to {cur_dst}\n")
        if item.is_dir():
            if not path.exists(cur_dst):
                mkdir(cur_dst)
                with open("./logs/copy_log.txt", "a") as file:
                    file.write(f"directory created: {cur_dst}\n")
            copy_static_to_public(cur_src, cur_dst)
           
            
def delete_directory(target):
    """
    Deletes the specified target directory if it exists.

    Parameters:
        target (str): The path to the directory to be deleted.

    Returns:
        None
    """
    items = scandir(target)
    for item in items:
        if item.is_dir():
            cur_target = path.join(target, item.name)
            rmtree(cur_target)
        else:
            remove(item)
    
    with open("./logs/copy_log.txt", "a") as file:
        file.write(f"\nNewly created at {dt.now()}")
