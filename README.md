# CLI Automated testing
This project automates the conda cli for creating environments, installing packages, and removing packages.  Python 3.5+ is required.

## Howto install conda
Refer to [conda documentation](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html)

## Howto install python dependencies for this test suite
### With conda:
```
# conda install anaconda::pytest
# conda install conda-forge::pytest-html
# conda install sphinx
# conda install conda-forge::sphinx-autodoc-typehints
# conda install conda-forge::just
```
### With pip:
`# pip install -f requirements.txt`

## Howto run the tests
`# pytest`

## Howto view the documentation
Auto generated code documentation can be view in [docs/_build/index.html](docs/_build/html/index.html)

## Howto regenerate documentation
`# cd docs`
`# make html`

## Howto look at the test report
A test report from the last pytest run can be found at [reports/report.html](reports/report.html)

## Project layout
Business logic for wrapping the conda CLI actions are in [conda_cli/run_conda.py](conda_cli/run_conda.py)
The actual tests for Create, Update, and Delete conda environments and packages are in [conda_tests/test_conda.py](conda_tests/test_conda.py)
The logger utility configuration is in [utils/logger.py](utils/logger.py)

## TODO
1. Wrap this project in a Docker container with alpine, python, and conda dependencies.
   1. Set up a conda local cache in the docker container to speed up the tests (currently ~1m each)
2. Create instances of data classes using dicts to deserialize for known tests.
