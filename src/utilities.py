# utilities.py

import os
import shutil

def check_dirs(source_dir, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)

def copy_files(source_path, dest_path):
    shutil.copy2(source_path, dest_path)