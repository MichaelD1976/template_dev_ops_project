# Makefile for template_dev_ops_project
# Provides simple commands to set up environment and run tests
# Contains a set of directives/commands. Typing 'make install' in bash will trigger the install commands etc

# # When initially creating a venv this is the Windows bash code
# # However we are creating this code within the install Makefile command as a short-cut
# python -m venv .venv
# .venv\Scripts\activate      # Windows
# pip install -r requirements.txt

# Path to virtual environment
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Create virtual environment if it doesn't exist, then install dependencies
install:
	if [ ! -d "$(VENV)" ]; then \
		python -m venv $(VENV); \
	fi
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run tests using pytest inside the virtual environment
test:
	$(PYTHON) -m pytest -q