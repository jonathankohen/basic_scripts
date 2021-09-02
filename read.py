"""Reads a given file and prints the content"""

import sys
import os


if len(sys.argv) <= 1:
    print("Usage: python3 read.py <file_name>")
    sys.exit(1)

if os.path.exists(sys.argv[1]):
    with open(sys.argv[1], "r") as f:
        print(f.read())
else:
    exit(1)
