# {{cookiecutter.repo_name}}
[![pytest](https://github.com/{{cookiecutter.username}}/{{cookiecutter.repo_name}}/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/{{cookiecutter.username}}/{{cookiecutter.repo_name}}/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/{{cookiecutter.pack_name}}.svg)](https://badge.fury.io/py/{{cookiecutter.pack_name}})

{{cookiecutter.repo_name}} descr

## Install it

```shell
pip install {{cookiecutter.pack_name}}
# or poetry add {{cookiecutter.pack_name}}
# pip install git+htts://github.com/{{cookiecutter.username}}/{{cookiecutter.pack_name}}
# poetry add git+htts://github.com/{{cookiecutter.username}}/{{cookiecutter.pack_name}}

# To upgrade
pip install {{cookiecutter.pack_name}} -U
# or poetry add {{cookiecutter.pack_name}}@latest
```

## Use it
```python
from {{cookiecutter.pack_name}} import {{cookiecutter.pack_name}}

```
