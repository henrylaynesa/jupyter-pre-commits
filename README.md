Jupyter Notebook Formatter
===============================

A [pre-commit](https://github.com/pre-commit) hook that will format each cell in Jupyter notebooks using [Black](https://github.com/psf/black).


Add this to your ``.pre-commit-config.yaml`` file

    - repo: git@github.com:henrylaynesa/notebook-formatter.git
      rev: master
      hooks:
      - id: notebook-formatter