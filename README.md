# Async Playwright SauceDemo Automation

An asynchronous UI automation project for SauceDemo, built with Python, Playwright's async API, and pytest. The framework uses the Page Object Model and JSON-driven user data to run multiple browser workflows concurrently.

## What it covers

- Runs workflows for `standard_user`, `locked_out_user`, `problem_user`, and `performance_glitch_user` using test data loaded from JSON.
- Uses `asyncio.gather()` to execute the four user workflows concurrently.
- Gives each workflow its own browser context and page to keep browser state isolated.
- Handles the locked-out and problem-user cases as expected by the test flow; the standard and performance-glitch user workflows proceed through checkout.
- Captures screenshots during the workflows and logs activity to `reports/automation.log`.
- Collects exceptions from concurrent workflows and closes browser contexts after execution.
- Uses Firefox for browser automation.

The project notes confirm that all four user workflows passed with screenshots and a log. The screenshot output path and exact test-module layout were not included in the available notes.

## Requirements

- Python
- `pytest`
- `pytest-asyncio`
- `playwright`
- Firefox browser binaries installed through Playwright

Install the Python dependencies from the project's `requirements.txt`:

```bash
pip install -r requirements.txt
```

Install Firefox for Playwright:

```bash
python -m playwright install firefox
```

## Run the tests

Run the project's pytest suite from the repository root:

```bash
pytest
```

## Project design

### Page Object Model

Page interactions are organized using the Page Object Model, keeping page-level actions separate from test workflow orchestration.

### JSON-driven test data

The workflows take their user data from JSON. The four supported SauceDemo user types are `standard_user`, `locked_out_user`, `problem_user`, and `performance_glitch_user`. Keep credentials and any other account-specific values in the project's test data rather than embedding them in the README.

### Concurrent workflows

The async runner uses `asyncio.gather()` to start the user workflows concurrently. Each workflow creates and uses its own browser context and page, avoiding shared session state between users. Exceptions are collected so failures can be logged alongside the workflow results.

### Logs and screenshots

Execution activity is written to `reports/automation.log`. Screenshots are captured by the workflows; their exact destination depends on the project configuration.

## Continuous integration

A CI job for this project needs to install the Python dependencies, install Playwright's Firefox browser binaries, and run pytest. The available project notes do not specify a workflow file or artifact-upload configuration.
