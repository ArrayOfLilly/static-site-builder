import os.path as path
from copystatic import copy_static_to_public, delete_directory
from generate_static import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    delete_directory(dir_path_public)
    copy_static_to_public(dir_path_static, dir_path_public)
    print()
    generate_pages_recursive(
        dir_path_content, 
        template_path,
        dir_path_public
    )


main()
