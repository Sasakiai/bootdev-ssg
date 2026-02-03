import os
import shutil

from page_gen import generate_pages_recursive
from textnode import TextNode, TextType

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def copy_static(source_path, destination_path):
    os.mkdir(destination_path)
    dir_content = os.listdir(source_path)

    for item in dir_content:
        src_item_path = os.path.join(source_path, item)
        dst_item_path = os.path.join(destination_path, item)

        if os.path.isfile(src_item_path):
            shutil.copy(src_item_path, dst_item_path)
        else:
            copy_static(src_item_path, dst_item_path)


def copy_content(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)

    copy_static(src, dst)


def main():
    copy_content(dir_path_static, dir_path_public)

    generate_pages_recursive(dir_path_content, template_path, dir_path_public)


if __name__ == "__main__":
    main()
