# AIDI2004 Lab 2 - Scenario 2 - Surender (Sunny) Dagar

CI pipeline with linting and testing for AIDI 2004.

**Student:** Surender (Sunny) Dagar
**Student ID:** 101036575

## Scenario 2: CI Pipeline with Linting and Testing
A Python calculator module with unit tests. A GitHub Actions workflow runs
`flake8` (linting) and `unittest` (tests) on every push, demonstrating both a
passing and a failing pipeline.

## Files
- `calculator.py` — add, subtract, multiply, divide functions.
- `test_calculator.py` — unit tests for the calculator.
- `requirements.txt` — declares `flake8`.
- `.github/workflows/sunny-ci.yml` — the CI workflow (lint + test).

## How the CI pipeline works
On every push, a GitHub-hosted Ubuntu runner:
1. Checks out the code.
2. Sets up Python 3.11.
3. Installs dependencies from `requirements.txt`.
4. Runs `flake8` to check code style (catches issues before production).
5. Runs the unit tests with `unittest`.

If linting or any test fails, the pipeline fails (red X). If everything
passes, the pipeline succeeds (green checkmark).
