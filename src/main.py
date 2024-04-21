import os.path as path
from copystatic import copy_static_to_public, delete_directory
from generate_static import generate_page


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    delete_directory(dir_path_public)
    copy_static_to_public(dir_path_static, dir_path_public)
    generate_page(
        path.join(dir_path_content, "index.md"),
        template_path,
        path.join(dir_path_public, "index.html"),
    )
           
main()





