## Purpose

This repository is a very small Python CLI quiz application implemented in a single file (`quiz.py`). The goal of these instructions is to give an AI coding agent the exact, discoverable knowledge needed to be productive immediately (no assumptions about hidden CI, builds or external services).

## Big-picture

- Single-file Python CLI: the app lives in `quiz.py`. There are no packages, modules, or external dependencies.
- Runtime: run directly with the system Python (Windows PowerShell in this workspace).

## Key file

- `quiz.py` — interactive script using `print()`, `input()`, `.lower()` and `quit()` for control flow. Example lines to reference:
  - Program prompts the user: `playing = input("Do you want to play?").lower()`
  - Exits if user doesn't answer `"yes"`: `if playing != "yes": quit()`
  - First question uses `.lower()` on the user answer: `answer = input("What does CPU stand for?").lower()`

## How to run (developer workflows)

- Run locally in PowerShell (workspace root):

  ```powershell
  python .\quiz.py
  ```

- There is no build step, no dependencies to install, and no test harness present.

## Conventions & patterns specific to this repo

- Keep UI as a simple synchronous CLI using `input()` and `print()`.
- Answers are normalized with `.lower()` before comparison — preserve that pattern for new prompts to keep UX consistent.
- The script currently uses `quit()` to terminate immediately when the player opts out — preserve this short-circuit behavior unless asked to refactor.

## Examples for code changes an agent might make

- Add a new question following the existing style: call `input(...)`, then `.lower()`, and compare against the expected lowercase answer.
- When adding multiple questions, prefer a minimal, backward-compatible refactor: extract a function like `ask_question(prompt, correct_answer)` but keep the top-level script interactive flow unchanged unless the user requests a non-interactive API.

## What to avoid

- Do not convert the program into a web app, GUI, or service without asking — this repository is explicitly a small CLI exercise.
- Avoid introducing dependencies unless there's a clear, documented need; this project has none now.

## Integration points / external dependencies

- None detected. No network, database, or external service integrations are present.

## When to ask the maintainer

- Before changing the UX (for example, replacing `input()` with command-line options or adding persistent scoring), ask whether the goal is to keep the CLI minimal or to extend it into a larger app.

## Quick edits that are safe and useful

- Small refactors that keep behavior identical (e.g., factoring repeated code into helper functions and adding docstrings).
- Add minimal unit tests (pytest) only after refactoring logic into pure functions; do not attempt to add tests that rely on stdin/stdout interactions without asking how the maintainer wants them structured.

If anything in these notes is unclear or you'd like the agent to follow a stricter/looser style (e.g., prefer functional refactors, add tests now, or keep absolutely minimal changes), tell me which direction and I will update this file.
