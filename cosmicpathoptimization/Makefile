PROGRAM = python3
FILE = cosmic_path.py
TEST_FILE = test_cosmic_path.py
SUBMIT_FILE = ../kattis-cli/submit.py

.PHONY: all
all: type style style-fix unittest test submit clean

.PHONY: type
type:
	mypy --strict $(FILE)
	mypy --strict $(TEST_FILE)

.PHONY: style
style:
	flake8 $(FILE)
	flake8 $(TEST_FILE)

.PHONY: style-fix
style-fix:
	autopep8 --in-place --recursive --aggressive --aggressive $(FILE)
	autopep8 --in-place --recursive --aggressive --aggressive $(TEST_FILE)

.PHONY: unittest
unittest:
	pytest

.PHONY: test
test:
	@cat 1.in | $(PROGRAM) $(FILE) | diff - 1.ans
	@echo "all tests done..."

.PHONY: submit
submit:
	$(SUBMIT_FILE) $(FILE)

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .hypothesis