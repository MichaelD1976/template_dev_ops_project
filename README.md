# Template DevOps Python Project

[![CI](https://github.com/MichaelD1976/template_dev_ops_project/actions/workflows/ci.yml/badge.svg)](https://github.com/MichaelD1976/template_dev_ops_project/actions/workflows/ci.yml)

This repository is a template Python project demonstrating a clean and maintainable project setup with basic DevOps and CI/CD practices. It includes a Python package, unit testing, automation via Makefile, a .gitignore to keep the repository clean, and a GitHub Actions CI workflow that automatically runs tests on push or pull request.

## Project Structure

The repository is organized as follows:

template_dev_ops_project/           # Repository root
├── template_dev_ops_project/       # Python package folder
│   ├── __init__.py                # Marks this folder as a package
│   └── main.py                     # Example functions
├── tests/                          # Unit tests
│   └── test_main.py                # Tests for main.py
├── .github/
│   └── workflows/
│       └── ci.yml                  # GitHub Actions CI workflow
├── requirements.txt                # List of dependencies
├── Makefile                        # Automation commands: install/test
├── .gitignore                       # Ignored files and folders
└── README.md                        # This documentation

## Python Package

All Python code lives inside the template_dev_ops_project/ folder. The __init__.py file marks it as a Python package, and main.py contains example functions. This package structure ensures clean imports and allows the project to be installed or packaged in the future.

## Tests

Unit tests are stored in the tests/ folder using pytest. Each test file mirrors the corresponding source file (e.g., test_main.py tests main.py). Keeping tests separate from source code ensures maintainability and clarity.

To run tests locally:

make test

## Makefile

The Makefile automates common development tasks:

make install – creates a virtual environment (if missing) and installs dependencies

make test – runs unit tests inside the virtual environment

Automation ensures consistent setup for all contributors and avoids repetitive commands.

## Setup.py
In small projects or when running scripts directly, a setup.py file is often not needed because Python can find files in the same folder. However, for structured projects and CI/CD workflows, setup.py (or pyproject.toml) is important: it tells Python that your project is an installable package, allows imports like from template_dev_ops_project import ... to work anywhere, and enables GitHub Actions to run tests in a clean environment. Installing the package locally with pip install -e . makes development easier by reflecting code changes immediately, and it also provides the metadata needed if you ever want to distribute the package.

## Requirements

Dependencies are listed in requirements.txt. Currently, only pytest is required for running tests. Additional packages (e.g., numpy, pandas) can be added here as the project grows.

## GitHub Actions CI

The workflow in .github/workflows/ci.yml enables continuous integration:

Triggered on pushes or pull requests to the main branch

Installs Python, installs dependencies, and runs all tests automatically

This provides immediate feedback about test success or failure, ensuring code changes are validated and reliable.

## Usage

Clone the repository:

git clone https://github.com/YOUR_USERNAME/template_dev_ops_project.git
cd template_dev_ops_project


## Install dependencies:

make install


## Run tests:

make test


Modify or add code in the package, add corresponding tests, and push changes. The CI workflow will automatically run the tests.

## Notes

.gitignore ensures virtual environments, Python caches, and editor settings are not committed.

The Python package folder ensures proper import paths and allows for future packaging.

This repository is intended as a reference template for small-to-medium Python projects with CI/CD.
