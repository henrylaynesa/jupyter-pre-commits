from __future__ import absolute_import, print_function, unicode_literals

import json


class Notebook:
    def __init__(self, path):
        self.path = path
        with open(path, "r") as f:
            self.json = json.load(f)

    def get_cells(self):
        return self.json["cells"]

    def get_cell(self, i):
        return self.get_cells()[i]

    def get_code_cells(self):
        cells = self.json["cells"]
        code_cells = [i for i, cell in enumerate(cells) if cell["cell_type"] == "code"]

        return code_cells

    def get_markdown_cells(self):
        cells = self.json["cells"]
        markdown_cells = [
            i for i, cell in enumerate(cells) if cell["cell_type"] == "markdown"
        ]

        return markdown_cells

    def get_raw_cells(self):
        cells = self.json["cells"]
        raw_cells = [i for i, cell in enumerate(cells) if cell["cell_type"] == "raw"]

        return raw_cells
