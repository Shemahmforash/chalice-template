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

## Code style

* Using `black` for the code style. Run `pre-commit install` to have a pre-commit that'll aplly the styling for you.

## Testing

* `pytest`
