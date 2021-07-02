# cookiecutter-poetry template
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Quick poetry/pytest/yarn/actions setup for a pypi project

## Usage

* Install `poetry` and `yarn` (or `npm`) the way you like it

* Run
```shell
pip install cookiecutter

# this creates the package directory structure according the `cookiecutter-poetry` template
cookiecutter gh:ffreemt/cookiecutter-poetry

# or cookiecutter https://github.com/ffreemt/cookiecutter-poetry.git
```

* cd to the package directory
```bash
cd pack_name
```
* Run
```bash
# this installs logzero, black, flake8, tbump, pep257, poethepoet given in pyproject.toml
poetry install

# this installs npm-run-all given in package.json
yarn  # or npm install
```

* Shortcuts are set in package.json. Take a look and get a rough idea. For example
   * `yarn style`: will run `black tests pack_name` and reload when any .py file is modified in `tests` and pack_name directories.

Now you have a project set up and can start coding and change the world for the better;).

