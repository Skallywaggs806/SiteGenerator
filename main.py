from src.markdown_to_html import markdown_to_html_node

import os
import shutil
import logging
import sys


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"


def copy_static_to_public():
    """
    Copy static files from the static directory to the public directory.
    """
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    public_dir = os.path.join(os.path.dirname(__file__), "docs")

    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    
    os.mkdir(public_dir)

    copy_recursive(static_dir, public_dir)


def copy_recursive(src, dst):
    """
    Recursively copy files and directories from src to dst.
    """
    if os.path.isdir(src):
        if not os.path.exists(dst):
            os.mkdir(dst)
            logging.info(f"Created directory: {dst}")
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            logging.info(f"Copying: {s} -> {d}")
            copy_recursive(s, d)
    else:
        shutil.copy2(src, dst)
        logging.info(f"Copied file: {src} -> {dst}")



def extract_title(markdown):
    """
    Extract the title from the markdown file.
    """
    with open(markdown, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("# "):
                return line[2:].strip()
    raise ValueError("No title found in the markdown file.")

def generate_page(from_path, template_path, dest_path):
    """
    Generate a page from a markdown file using a template.
    """
    print(f"Generating page from {from_path} using template {template_path} to {dest_path}")

    with open(from_path, "r") as f:
        content = f.read()

    title = extract_title(from_path)

    with open(template_path, "r") as f:
        template = f.read()


    html_node = markdown_to_html_node(content)
    page_content = html_node.to_html()
    html_content = template.replace("{{ Title }}", title).replace("{{ Content }}", page_content)
    html_content = html_content.replace('href="/"', f'href="{basepath}"').replace('src="/"', f'src="{basepath}"')

    with open(dest_path, "w") as f:
        f.write(html_content)
        logging.info(f"Generated page: {dest_path}")


def generate_pages_recursive(dir_path_content, template_path, dest_path_dir):
    """
    Recursively generate pages from markdown files in a directory.
    """
    if not os.path.exists(dest_path_dir):
        os.mkdir(dest_path_dir)
        logging.info(f"Created directory: {dest_path_dir}")

    for item in os.listdir(dir_path_content):
        src_item = os.path.join(dir_path_content, item)
        dest_item = os.path.join(dest_path_dir, item)

        if os.path.isdir(src_item):
            generate_pages_recursive(src_item, template_path, dest_item)
        elif item.endswith(".md"):
            generate_page(src_item, template_path, dest_item.replace(".md", ".html"))



def main():
    output_dir = "docs"  # Changed from "public"
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    
    copy_static_to_public()
    print("Static files copied to docs directory.")
    generate_pages_recursive("content", "template.html", output_dir)

    




if __name__ == "__main__":
    main()
