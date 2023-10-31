PROGRAM = python3
FILE = cosmic_path.py
TEST_FILE = test_cosmic_path.py
SUBMIT_FILE = ../kattis-cli/submit.py

all: type style style-fix unittest test clean

type:
	mypy $(FILE)
	mypy $(TEST_FILE)

style:
	flake8 $(FILE)
	flake8 $(TEST_FILE)

style-fix:
	autopep8 --in-place --recursive --aggressive --aggressive $(FILE)
	autopep8 --in-place --recursive --aggressive --aggressive $(TEST_FILE)

unittest:
	pytest

test:
	@cat 1.in | $(PROGRAM) $(FILE) | diff - 1.ans
	@echo "all tests done..."

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .hypothesis