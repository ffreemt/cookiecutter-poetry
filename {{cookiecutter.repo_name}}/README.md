# {{cookiecutter.pack_name}}
[![tests](https://github.com/{cookiecutter.username}/{{cookiecutter.repo_name}}/actions/workflows/routine-tests.yml/badge.svg)][![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/{{cookiecutter.pack_name}}.svg)](https://badge.fury.io/py/{{cookiecutter.pack_name}})

Quick poetry/pytest/yarn/actions setup for a pypi project

## Usage

```shell
pip install cookiecutter

cookiecutter gh:ffreemt/cookiecutter-poetry
# or cookiecutter https://github.com/ffreemt/cookiecutter-poetry.git

# cd pack_name

poetry install
yarn
```