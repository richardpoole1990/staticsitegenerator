import os
import shutil
import sys

from utilities import check_dirs, copy_files
from page_generator import generate_pages_recursive

def main():
    source = "static"
    destination = "docs"

    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"

    # 1. Delete everything in `public`
    if os.path.exists(destination):
        print("Destination directory already exists. Deleting it.")
        shutil.rmtree(destination)

    # Recreate the public directory
    os.makedirs(destination, exist_ok=True)

    # 2. Copy all static files *after* deleting the public directory
    if os.path.exists(source):
        for item in os.listdir(source):
            source_path = os.path.join(source, item)
            destination_path = os.path.join(destination, item)
            if os.path.isdir(source_path):
                shutil.copytree(source_path, destination_path)
            else:
                shutil.copy2(source_path, destination_path)

    # 3. Generate pages recursively
    generate_pages_recursive(
        dir_path_content="content",
        template_path="template.html",
        dest_dir_path="docs",
        base_path=base_path
    )

if __name__ == "__main__":
    main()