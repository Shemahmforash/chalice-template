# Chalice template

## Requirements

* python 3.7
* pipenv - <https://pipenv.readthedocs.io/en/latest/#install-pipenv-today>
* In order to do a deploy you'll need aws cli setup

## Installation

* Clone the project
* Install all dependencies (including dev ones) `pipenv install --dev`
* Test that everything is ok by running: `pipenv run chalice local`

## Code style

* Using `black` for the code style. Run `pipenv run pre-commit install` to have a pre-commit that'll aplly the styling for you.

## Testing

* `pipenv run pytest`

## Tips

* To open a buffer with the virtual environment auto activated do `pipenv shell`. In this way you don't need to prefix all commands with `pipenv run`.
