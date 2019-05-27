# Chalice template

## Requirements

* python 3.7
  * https://docs.python-guide.org/starting/install3/osx/
* In order to do a deploy you'll need aws cli setup

## Installation

* Clone the project
* Create a virtual environment and activate it
* Install all dependencies (including dev ones) `pip install -r requirements.txt ; pip install -r requirements-dev.txt`
* Test that everything is ok by running: `chalice local`

## Chalice documentation

* It'll be helpful to check chalice documentation at https://github.com/aws/chalice and https://chalice.readthedocs.io/en/latest/

## Code style and type checks

* There's a pre-commit hook that'll enforce the code styling (using `black` and `isort`) and verify typings (using `mypy`). Run `pre-commit install` to install it.

## Testing

* `pytest`
