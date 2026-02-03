import os

from markdown_parser import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()

    raise ValueError("No title found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = open(from_path, "r").read()
    template = open(template_path, "r").read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)
        f.close()
