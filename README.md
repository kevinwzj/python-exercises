# Python Exercises

A tiny exercise repository for practicing small Python programs and pytest.

Prerequisites
- Python 3.8+ (3.11+ recommended)
- git

Quick setup
1. python -m venv .venv
2. Windows: .venv\Scripts\activate
   macOS / Linux: source .venv/bin/activate
3. pip install -r requirements.txt
4. (Recommended for development) pip install -r dev-requirements.txt

Running tests
- Run the full test suite:
  python -m pytest -q
- Run a single test:
  python -m pytest tests/test_exercise1.py::test_greet -q

Coverage
- Dev requirements include pytest-cov and coverage. Generate reports with:
  python -m pytest --cov=exercises --cov-report=term --cov-report=html -q
- HTML report is written to htmlcov/index.html
- A .coveragerc is present to omit tests, venv, and other noise from reports
- CI uploads coverage.xml and the htmlcov folder as artifacts named `coverage-xml` and `coverage-html`

Formatting, linting and type checking
- Format: black .
- Import sorting: isort .
- Lint: flake8 .
- Type-check: mypy .
- Recommended dev tools (dev-requirements.txt): black, isort, flake8, mypy, pytest, pytest-cov, coverage

CI (GitHub Actions)
- Workflow: .github/workflows/ci.yml
- Runs on Windows (windows-latest) across Python versions (matrix)
- Installs dev-requirements.txt if present, otherwise installs tools on the fly
- Steps: black --check, flake8, mypy, pytest with coverage
- CI publishes coverage.xml and htmlcov as artifacts named `coverage-xml` and `coverage-html`

Repository notes
- Runtime requirements: none (requirements.txt kept minimal)
- Development requirements: dev-requirements.txt
- .gitignore updated to ignore .venv, htmlcov, coverage.xml, .coverage, IDE files, caches, and pip artifacts
- Tests live in tests/ and aim to keep functions small and pure for easy unit testing

Contributing
- Branch from main and open PRs
- Run locally: black . && isort . && flake8 . && python -m pytest
- Use conventional commits for clear history (feat/, fix/, docs/, chore/)

License
- MIT (replace with your preferred license)
