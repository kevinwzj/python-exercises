# Python Exercises

A tiny exercise repository for practicing Python and pytest.

Prerequisites
- Python 3.8+ (3.11+ recommended)
- git

Setup
- python -m venv .venv
- .venv/Scripts/activate   (Windows)
- pip install -r requirements.txt
- pip install -r dev-requirements.txt  # optional: dev tools (black, flake8, mypy, pytest-cov)

Running tests
- Run the full test suite: python -m pytest -q
- Run a single test: python -m pytest tests/test_exercise1.py::test_greet -q

Coverage
- Install coverage tools: pip install -r dev-requirements.txt (or pip install pytest-cov coverage)
- Run coverage and generate HTML report:
  python -m pytest --cov=exercises --cov-report=term --cov-report=html -q
- Open the HTML report at htmlcov/index.html
- Note: a .coveragerc is included to omit tests and virtualenv files from the report

Formatting and linting
- Format: black .
- Lint: flake8 .
- Type-check: mypy .
- Recommended dev tools: black, flake8, mypy, isort, pytest-cov

Adding tests
- Place tests in the tests/ directory using pytest conventions.
- Keep tests deterministic and fast.
- Prefer unit-testing pure functions; use subprocess for CLI scripts when necessary.

Continuous Integration
- Add a GitHub Actions workflow that runs: black --check, flake8, mypy, and pytest --cov on push and PRs.

Contributing
- Create feature branches from main
- Run: black . && flake8 && python -m pytest before opening a PR
- Use conventional commit messages (feat/, fix/, docs/, chore/, etc.)

License
- MIT (replace with your preferred license)
