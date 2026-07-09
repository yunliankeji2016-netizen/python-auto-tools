# Copyright (c) 2026 yunliankeji2016-netizen
# SPDX-License-Identifier: MIT
import os

def scan_folder(target_dir):
    """Traverse folder and count total files for office sorting"""
    total = 0
    for root, dirs, files in os.walk(target_dir):
        total += len(files)
    return total

if __name__ == "__main__":
    target_path = "./work_files"
    count = scan_folder(target_path)
    print(f"Total files detected: {count}")
