# setup.py - tells Python and pip how to install your project

# Import the necessary functions from setuptools
from setuptools import setup, find_packages

# Call setup() to define your package
setup(
    # Name of your package/project
    name="template_dev_ops_project",

    # Version of your package
    version="0.1.0",

    # Automatically find all Python packages in your project
    # A "package" is a folder containing __init__.py
    packages=find_packages(),

    # Optional: list dependencies that pip should install
    # Example: install_requires=["numpy", "pandas"]
    install_requires=[],

    # Optional: short description of your project
    description="A template Python project with DevOps and CI/CD setup",

    # Optional: author information
    author="Michael D.",
    author_email="michaeldearlove@yahoo.co.uk",

    # Optional: the license for your project
    license="MIT",

    # Optional: README file
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",

    # Optional: Python version requirement
    python_requires=">=3.11",

    # Optional: keywords for PyPI (if you publish)
    keywords="template devops ci cd python",

    # Optional: URL of project homepage or repo
    url="https://github.com/MichaelD1976/template_dev_ops_project",
)
