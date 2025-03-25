import os
import shutil
from markdown_blocks import markdown_to_html_node
from utilities import check_dirs, copy_files

def extract_title(markdown):
    old_text = markdown
    raise_error = True
    title = ""

    for line in old_text.splitlines():
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            title = line.replace("#", '')
            title = title.strip()
            raise_error = False
            return title
    if raise_error:
        raise ValueError("invalid markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file
    with open(from_path, 'r') as f:
        markdown_content = f.read()

    # Read the template file
    with open(template_path, 'r') as f:
        template_content = f.read()

    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Extract title
    title = extract_title(markdown_content)

    # Replace placeholders in template
    full_html = template_content.replace('{{ Title }}', title).replace('{{ Content }}', html_content)

    # Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write output file
    with open(dest_path, 'w') as f:
        f.write(full_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Create the destination directory if it doesn't exist
    os.makedirs(dest_dir_path, exist_ok=True)
    print(f"Processing directory: {dir_path_content}")

    # Loop through items in the directory
    for item in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        # Debugging message for each file/directory
        print(f"Found item: {source_path} (Destination: {dest_path})")

        # If item is a directory, recursively process it
        if os.path.isdir(source_path):
            print(f"Entering directory: {source_path}")
            generate_pages_recursive(source_path, template_path, dest_path)
        else:
            # Handle markdown files
            if item.endswith('.md'):
                # Change the file extension from .md to .html
                base_name, ext = os.path.splitext(dest_path)
                dest_path = f"{base_name}.html"
                print(f"Generating page: {source_path} -> {dest_path}")
                generate_page(source_path, template_path, dest_path)
            else:
                # Non-markdown files—copy without transformation
                print(f"Copying file: {source_path} -> {dest_path}")
                os.makedirs(dest_dir_path, exist_ok=True)
                copy_files(source_path, dest_path)
