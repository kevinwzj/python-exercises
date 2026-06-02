# Python Exercises

A tiny exercise repository for practicing Python and pytest.

Setup
- python -m venv .venv
- .venv\Scripts\activate
- pip install -r requirements.txt

Run tests
- pytest

Exercise
- Implement the function(s) in the exercises/ directory so all tests pass.

## Build & Test Commands
- python -m venv .venv
- .venv\Scripts\activate  (Windows)
- pip install -r requirements.txt
- python -m pytest -q

## Code Style
- Follow PEP 8 style guide
- Use type hints and docstrings for public functions
- Use black for formatting and flake8 for linting

## Workflow
- Run `black . && flake8 && python -m pytest` after making changes
- Commit messages follow conventional commits format
- Create feature branches from `main`
