import os

from markdown_parser import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()

    raise ValueError("No title found")


def generate_page(basepath, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = open(from_path, "r").read()
    template = open(template_path, "r").read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)
        f.close()


"""
os.listdir: lists the files inside the given directory
os.path.join: concatenate path segments
os.path.isfile: returns true if the given path is a file
pathlib.Path: the Path class
"""


def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    content = os.listdir(dir_path_content)

    for item in content:
        item_src_path = os.path.join(dir_path_content, item)

        if os.path.isfile(item_src_path):
            if item.endswith(".md"):
                generate_page(
                    basepath,
                    item_src_path,
                    template_path,
                    os.path.join(dest_dir_path, "index.html"),
                )
        else:
            generate_pages_recursive(
                basepath,
                item_src_path,
                template_path,
                os.path.join(dest_dir_path, item),
            )
