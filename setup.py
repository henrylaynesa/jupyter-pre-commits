import sys
from distutils.core import setup

from setuptools import find_packages

install_requires = ["black==19.10b0,<20", "isort>=4.1.1,<5"]
if sys.version_info < (2, 7):
    install_requires.append("argparse")

setup(
    name="Black Notebook",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "black_notebook = jupyter_precommit.black_notebook:main"
        ]
    },
)
