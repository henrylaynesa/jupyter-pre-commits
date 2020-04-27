from __future__ import absolute_import, print_function, unicode_literals

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="+", help="Jupyter notebook filenames")
    args = parser.parse_args()

    retv = 0
    for filename in args.filenames:
        with open(filename, "r") as f:
            try:
                json.load(f)
            except (ValueError, UnicodeDecodeError) as e:
                print(f"{filename}: Failed to json decode ({e})")
                retv = 1
    return retv


if __name__ == "__main__":
    exit(main())
