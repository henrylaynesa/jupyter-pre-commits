from __future__ import absolute_import, print_function, unicode_literals

import argparse
import json
from pathlib import Path
from subprocess import PIPE, Popen


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="+", help="Jupyter notebook filenames")
    parser.add_argument(
        "--pre-commit", action="store_true", dest="pre_commit", help="Use as Pre-commit"
    )
    parser.add_argument(
        "--disable-black",
        action="store_true",
        dest="disable_black",
        help="Disable black from being applied to Jupyter notebook",
    )
    # parser.add_argument(
    #     "--disable-isort",
    #     action="store_true",
    #     dest="disable_isort",
    #     help="Disable isort from being applied to Jupyter notebook",
    # )
    args = parser.parse_args()

    if args.pre_commit:
        proc = Popen(
            ["git", "diff", "--staged", "--name-only", "--diff-filter=A"],
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
        )
        stdout, stderr = proc.communicate()
        filenames = stdout.decode().splitlines()

    for filename in args.filenames:
        if not filename.endswith(".ipynb"):
            raise Exception(f"Non-Jupyter notebook file {filename} found")
    filenames = args.filenames

    if len(filenames) == 0:
        return 0

    retv = 0

    for filename in filenames:
        with open(filename, "r") as f:
            notebook = json.load(f)
        for i, cell in enumerate(notebook["cells"]):
            cell_source = "".join(cell["source"])

            # Black
            if not args.disable_black:
                proc = Popen(
                    ["black", "-c", cell_source], stdin=PIPE, stdout=PIPE, stderr=PIPE
                )
                stdout, stderr = proc.communicate()
                if stderr.decode() != "":
                    raise Exception(stderr.decode())
                stdout = stdout.decode().strip()
                delim = "\n"
                new_source = [line + delim for line in stdout.split("\n")]
                new_source[-1] = new_source[-1].strip()

            if cell_source != stdout:
                notebook["cells"][i]["source"] = new_source
                retv = 1
        with open(filename, "w") as f:
            json.dump(notebook, f)
    return retv


if __name__ == "__main__":
    exit(main())
