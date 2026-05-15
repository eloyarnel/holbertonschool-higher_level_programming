# Python – Test-Driven Development

## Description

This project focuses on writing Python functions using a **test-driven development (TDD)** approach.
The main goal is to write tests first (doctests and unittests), then implement functions that pass those tests while following strict coding standards.

## Learning Objectives

* Understand the principles of Test-Driven Development (TDD)
* Write and interpret doctests
* Create unit tests using the `unittest` module
* Handle exceptions properly in Python
* Write clean, documented, PEP8-compliant code
* Improve code reliability through systematic testing

## Requirements

### Python Scripts

* Ubuntu 20.04 LTS
* Python 3.8.5
* Editors allowed: `vi`, `vim`, `emacs`
* First line of each file:

  ```python
  #!/usr/bin/python3
  ```
* Files must end with a new line
* Code must follow **pycodestyle 2.7.***
* All files must be executable
* Every module and function must have proper documentation

### Tests

* Tests stored inside a `tests/` directory
* Doctest files must use `.txt`
* Unittests must use `.py`
* Run doctests:

  ```bash
  python3 -m doctest ./tests/*
  ```
* Run unittests:

  ```bash
  python3 -m unittest tests.*
  ```

## Main Tasks

Typical exercises include:

* Integer addition with validation (`add_integer`)
* Matrix division with error handling (`matrix_divided`)
* String formatting functions (`say_my_name`)
* Text formatting and indentation
* Printing shapes (`print_square`)
* Finding maximum values (`max_integer`)
* Writing both doctests and unittests

## Project Structure

```
.
├── *.py
├── tests/
│   ├── *.txt
│   └── *_test.py
└── README.md
```

## Author

Eloy A. Alicea Sanchez
