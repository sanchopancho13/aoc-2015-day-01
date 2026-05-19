# Advent of Code — Python template

Starter layout for solving [Advent of Code](https://adventofcode.com/) puzzles in Python: separate solution modules, `main1` / `main2` runners, pytest tests, and a small logging helper.

Solution and test files ship as stubs (`solution1`, `solution2`, and placeholder tests). Implement them for each puzzle you tackle.

## Create a new day repo from the template

Use one repo per puzzle day (for example `aoc-2026-day-03`).

### GitHub website

1. Open the template repo on GitHub.
2. Click **Use this template** → **Create a new repository**.
3. Name the repo (for example `aoc-2026-day-03`), choose visibility, and create it.
4. Clone the new repo locally.

### GitHub CLI

```bat
gh repo create aoc-2026-day-03 --template sanchopancho13/aoc-template --public --clone
```

### First-time setup

Requires **Python 3.10+**.

```bat
cd aoc-2026-day-03

# Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

On macOS or Linux:

```bash
cd aoc-2026-day-03
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

VS Code/Cursor users: `.vscode/settings.json` points the interpreter at `.venv`; reload the window after creating the venv.

## Project layout

```
.
├── main1.py              # Run part 1 (reads puzzle input path from argv)
├── main2.py              # Run part 2
├── solutions/
│   ├── part1.py          # solution1(input) -> result
│   └── part2.py          # solution2(input) -> result
├── tests/
│   ├── test_part1.py     # Unit tests for part 1
│   └── test_part2.py     # Unit tests for part 2
├── util/
│   └── utils.py          # @entry_point: argv check, logging, timing
├── test.txt              # Sample input for local runs (add your own)
├── requirements.txt      # pytest
└── pytest.ini            # testpaths + pythonpath
```

Put your downloaded puzzle input in `input.txt` (gitignored). Use `test.txt` (or another file) for examples while developing.

`main1.py` and `main2.py` convert an input file into the format to be passed to `solution1` / `solution2`.

## Common commands

Activate the venv first (`.\.venv\Scripts\Activate.ps1`).

| Task | Command |
|------|---------|
| Run all tests | `pytest` |
| Run tests with output | `pytest -v` |
| Run one test file | `pytest tests/test_part1.py` |
| Run part 1 on sample input | `python main1.py test.txt` |
| Run part 2 on sample input | `python main2.py test.txt` |
| Run on real input | `python main1.py input.txt` |
| Verbose logging | `python main1.py test.txt --debug` |

`@entry_point` requires an input file as the first argument. Running without one prints usage and exits with code 1:

```text
Usage: main1.py <input-file> [--debug]
```

## Typical workflow for a new day (TDD)

Work one part at a time: part 1 through green tests, then part 2.

1. **Name and type the API** — Rename `solution1` and `solution2` to descriptive names (for example `count_safe_reports`). Set parameter and return types to match the puzzle (for example `def count_safe_reports(lines: list[str]) -> int`). Update imports in `main1.py`, `main2.py`, and the test modules. Adjust `main*.py` input parsing so it builds whatever shape your functions expect (a single `str`, `list[str]`, a parsed grid, and so on).
2. **Red** — Replace the placeholder tests in `tests/test_part1.py` with examples from the puzzle statement. Call your renamed function with the typed inputs; assert the expected outputs. Run `pytest`; tests should fail against the stub implementation.
3. **Green** — Implement the function in `solutions/part1.py` until `pytest` passes.
4. **Refactor** — Clean up the solution or tests if needed; keep `pytest` green.
5. Repeat steps 2–4 for part 2 in `tests/test_part2.py` and `solutions/part2.py`.
6. Add puzzle examples to `test.txt` (or another sample file) and run `python main1.py test.txt` / `python main2.py test.txt` to exercise the full read → solve path.
7. Download your input from Advent of Code into `input.txt`, then run `python main1.py input.txt` and `python main2.py input.txt` for answers.
