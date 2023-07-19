# Signifies our desired python version
# Makefile macros (or variables) are defined a little bit differently than traditional bash, keep in mind that in the Makefile there's top-level Makefile-only syntax, and everything else is bash script syntax.
PYTHON = python3

# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY = all help install venv test run clean

# Defining an array variable
FILES = input output

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

# define the name of the virtual environment directory
VENV := venv

# default target, when make executed without arguments
all: install run clean

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "---------------HELP-----------------"
	@echo "make install"
	@echo "     prepare development environment, use only once"
	@echo "make test"
	@echo "     run tests"
	@echo "make lint"
	@echo "     run pylint and mypy"
	@echo "make run"
	@echo "     run project"
	@echo "make doc"
	@echo "     build sphinx documentation"
	@echo "------------------------------------"

install:
	sudo apt-get -y install python3.5 python3-pip
	${PYTHON} -m $(VENV) $(VENV)
# This generates the desired project file structure
# A very important thing to note is that macros (or makefile variables) are referenced in the target's code with a single dollar sign ${}, but all script variables are referenced with two dollar signs $${}
#setup:
#	
#	@echo "Checking if project files are generated..."
#	[ -d project_files.project ] || (echo "No directory found, generating..." && mkdir project_files.project)
#	for FILE in ${FILES}; do \
#		touch "project_files.project/$${FILE}.txt"; \
#	done
init:
	: # Activate venv and install smthing inside
	. ../$(VENV)/bin/activate && pip install -r requirements.txt
	: # Other commands here
# venv is a shortcut target
venv: init
	( \
	. ../$(VENV)/bin/activate; \
	pip install -r requirements.txt; \
	)

run: venv
	( \
	. ../$(VENV)/bin/activate; \
	${PYTHON}  ./src/imgdetect/LaunchModel.py; \
	)


# The ${} notation is specific to the make syntax and is very similar to bash's $() 
# This function uses pytest to test our source files
test: venv
	( \
	. ../$(VENV)/bin/activate; \
	${PYTHON} './src/imgdetect/test.py'; \
	)
clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

