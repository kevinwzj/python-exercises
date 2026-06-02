# Python Exercises

A tiny exercise repository for practicing Python and pytest.

Prerequisites
- Python 3.8+ (3.11+ recommended)
- git

Setup
- python -m venv .venv
- .venv/Scripts/activate   (Windows)
- pip install -r requirements.txt
- (optional) pip install -r dev-requirements.txt

Running tests
- Run the full test suite: python -m pytest -q
- Run a single test: python -m pytest tests/test_exercise1.py::test_greet -q

Formatting and linting
- Format: black .
- Lint: flake8 .
- Type-check: mypy .
- Recommended dev tools: black, flake8, mypy, isort

Adding tests
- Place tests in the tests/ directory using pytest conventions.
- Keep tests deterministic and fast.
- Use subprocess to test CLI scripts when needed.

Continuous Integration (suggestion)
- Add a GitHub Actions workflow that runs: black --check, flake8, mypy, and pytest on push and PRs.

Contributing
- Create feature branches from main
- Run: black . && flake8 && python -m pytest before opening a PR
- Use conventional commit messages (feat/, fix/, docs/, chore/, etc.)

License
- MIT (replace with your preferred license)
