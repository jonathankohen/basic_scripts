"""Appends content to the end of a given file"""

import sys
import os


if len(sys.argv) <= 1:
    print("Usage: python3 write.py <file_name> '<string>'")
    sys.exit(1)

if os.path.exists(sys.argv[1]):
    with open(sys.argv[1], "a") as f:
        f.write(f"{sys.argv[2]}")
else:
    exit(1)
