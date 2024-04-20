from copystatic import copy_static_to_public, delete_directory


dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    delete_directory(dir_path_public)
        
    print("Copying static files to public directory...")
    copy_static_to_public(dir_path_static, dir_path_public)

           
main()





